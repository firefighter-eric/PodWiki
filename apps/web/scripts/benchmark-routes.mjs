import http from "node:http";

const oldBase = process.env.OLD_BASE ?? "http://127.0.0.1:3011";
const newBase = process.env.NEW_BASE ?? "http://127.0.0.1:3012";
const warmups = Number(process.env.PERF_WARMUPS ?? 5);
const samples = Number(process.env.PERF_SAMPLES ?? 40);

if (!Number.isInteger(warmups) || warmups < 0) {
  throw new Error("PERF_WARMUPS must be a non-negative integer");
}
if (!Number.isInteger(samples) || samples < 1) {
  throw new Error("PERF_SAMPLES must be a positive integer");
}

const oldAgent = new http.Agent({ keepAlive: true, maxSockets: 1 });
const newAgent = new http.Agent({ keepAlive: true, maxSockets: 1 });
const routes = [
  {
    name: "show",
    oldPath: "/shows/latetalk",
    newPath: "/shows/latetalk",
  },
  {
    name: "summary",
    oldPath: "/shows/latetalk/episodes/178-tian-yuandong?view=summary",
    newPath: "/shows/latetalk/episodes/178-tian-yuandong",
  },
  {
    name: "transcript",
    oldPath: "/shows/latetalk/episodes/178-tian-yuandong?view=transcript",
    newPath: "/shows/latetalk/episodes/178-tian-yuandong/transcript",
  },
];

function requestOnce(url, agent) {
  return new Promise((resolve, reject) => {
    const startedAt = performance.now();
    const request = http.get(url, {
      agent,
      headers: {
        accept: "text/html",
        "accept-encoding": "identity",
        "user-agent": "PodWiki-local-perf/1.0",
      },
    }, (response) => {
      const ttfbMs = performance.now() - startedAt;
      let bytes = 0;
      response.on("data", (chunk) => {
        bytes += chunk.length;
      });
      response.on("end", () => resolve({
        status: response.statusCode,
        ttfbMs,
        totalMs: performance.now() - startedAt,
        bytes,
        cacheControl: response.headers["cache-control"] ?? null,
      }));
    });
    request.on("error", reject);
  });
}

function median(values) {
  const sorted = values.toSorted((left, right) => left - right);
  const middle = Math.floor(sorted.length / 2);
  return sorted.length % 2 === 0
    ? (sorted[middle - 1] + sorted[middle]) / 2
    : sorted[middle];
}

function nearestRank(values, percentile) {
  const sorted = values.toSorted((left, right) => left - right);
  return sorted[Math.max(0, Math.ceil(percentile * sorted.length) - 1)];
}

function summarize(values) {
  return {
    samples: values.length,
    medianMs: median(values),
    p95Ms: nearestRank(values, 0.95),
    minMs: Math.min(...values),
    maxMs: Math.max(...values),
  };
}

const results = {};

try {
  for (const route of routes) {
    for (let index = 0; index < warmups; index += 1) {
      await requestOnce(oldBase + route.oldPath, oldAgent);
      await requestOnce(newBase + route.newPath, newAgent);
    }

    const raw = { old: [], new: [] };
    for (let index = 0; index < samples; index += 1) {
      const order = index % 2 === 0 ? ["old", "new"] : ["new", "old"];
      for (const variant of order) {
        const old = variant === "old";
        const sample = await requestOnce(
          (old ? oldBase : newBase) + (old ? route.oldPath : route.newPath),
          old ? oldAgent : newAgent,
        );
        if (sample.status !== 200) {
          throw new Error(`${route.name}/${variant} returned HTTP ${sample.status}`);
        }
        raw[variant].push(sample);
      }
    }

    const oldTtfb = summarize(raw.old.map((sample) => sample.ttfbMs));
    const newTtfb = summarize(raw.new.map((sample) => sample.ttfbMs));
    const oldTotal = summarize(raw.old.map((sample) => sample.totalMs));
    const newTotal = summarize(raw.new.map((sample) => sample.totalMs));

    results[route.name] = {
      old: {
        ttfb: oldTtfb,
        total: oldTotal,
        bytes: raw.old[0].bytes,
        cacheControl: raw.old[0].cacheControl,
      },
      new: {
        ttfb: newTtfb,
        total: newTotal,
        bytes: raw.new[0].bytes,
        cacheControl: raw.new[0].cacheControl,
      },
      medianTtfbReductionPercent: (1 - newTtfb.medianMs / oldTtfb.medianMs) * 100,
      p95TtfbReductionPercent: (1 - newTtfb.p95Ms / oldTtfb.p95Ms) * 100,
    };
  }

  process.stdout.write(`${JSON.stringify({
    environment: { oldBase, newBase, warmups, samples, node: process.version },
    results,
  }, null, 2)}\n`);
} finally {
  oldAgent.destroy();
  newAgent.destroy();
}
