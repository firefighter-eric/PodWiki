import { afterEach, describe, expect, it } from "vitest";
import {
  clearLocalStorageFallbackForTests,
  readLocalStorage,
  writeLocalStorage,
} from "@/lib/safe-storage";

afterEach(() => {
  clearLocalStorageFallbackForTests();
});

describe("safe local storage", () => {
  it("reads and writes through an available storage implementation", () => {
    const values = new Map<string, string>();
    const storage = {
      getItem: (key: string) => values.get(key) ?? null,
      setItem: (key: string, value: string) => values.set(key, value),
    };

    expect(readLocalStorage("reader", "default", storage)).toBe("default");
    expect(writeLocalStorage("reader", "large", storage)).toBe(true);
    expect(readLocalStorage("reader", "default", storage)).toBe("large");
  });

  it("keeps the current-session value when storage throws SecurityError", () => {
    const securityError = new DOMException("Access denied", "SecurityError");
    const blockedStorage = {
      getItem: () => {
        throw securityError;
      },
      setItem: () => {
        throw securityError;
      },
    };

    expect(readLocalStorage("reader", "default", blockedStorage)).toBe("default");
    expect(writeLocalStorage("reader", "wide", blockedStorage)).toBe(false);
    expect(readLocalStorage("reader", "default", blockedStorage)).toBe("wide");
  });
});
