"use client";

import { TextAlignCenter, TextAlignLeft, TextAlignRight } from "@phosphor-icons/react";
import { createContext, useCallback, useContext, useMemo, useSyncExternalStore } from "react";

type FontSize = "small" | "medium" | "large";
type Measure = "narrow" | "standard" | "wide";

type ReaderSettings = {
  fontSize: FontSize;
  measure: Measure;
  setFontSize: (value: FontSize) => void;
  setMeasure: (value: Measure) => void;
};

const defaultSettings: Pick<ReaderSettings, "fontSize" | "measure"> = {
  fontSize: "medium",
  measure: "standard",
};

const ReaderSettingsContext = createContext<ReaderSettings | null>(null);
const settingsStorageKey = "podwiki.reader.v1";
const defaultSnapshot = JSON.stringify(defaultSettings);

function parseSettings(snapshot: string): Pick<ReaderSettings, "fontSize" | "measure"> {
  try {
    const stored = JSON.parse(snapshot) as { fontSize?: FontSize; measure?: Measure };
    return {
      fontSize: stored.fontSize && ["small", "medium", "large"].includes(stored.fontSize)
        ? stored.fontSize
        : defaultSettings.fontSize,
      measure: stored.measure && ["narrow", "standard", "wide"].includes(stored.measure)
        ? stored.measure
        : defaultSettings.measure,
    };
  } catch {
    return defaultSettings;
  }
}

export function ReaderPreferences({ children }: { children: React.ReactNode }) {
  const subscribe = useCallback((callback: () => void) => {
    const handleChange = () => callback();
    window.addEventListener("storage", handleChange);
    window.addEventListener("podwiki-reader-change", handleChange);
    return () => {
      window.removeEventListener("storage", handleChange);
      window.removeEventListener("podwiki-reader-change", handleChange);
    };
  }, []);
  const snapshot = useSyncExternalStore(
    subscribe,
    () => window.localStorage.getItem(settingsStorageKey) ?? defaultSnapshot,
    () => defaultSnapshot,
  );
  const { fontSize, measure } = useMemo(() => parseSettings(snapshot), [snapshot]);

  const persist = (nextFontSize: FontSize, nextMeasure: Measure) => {
    window.localStorage.setItem(
      settingsStorageKey,
      JSON.stringify({ fontSize: nextFontSize, measure: nextMeasure }),
    );
    window.dispatchEvent(new Event("podwiki-reader-change"));
  };

  const value = useMemo<ReaderSettings>(
    () => ({
      fontSize,
      measure,
      setFontSize: (next) => persist(next, measure),
      setMeasure: (next) => persist(fontSize, next),
    }),
    [fontSize, measure],
  );

  return (
    <ReaderSettingsContext.Provider value={value}>
      <div className="episode-reader" data-font-size={fontSize} data-measure={measure}>
        {children}
      </div>
    </ReaderSettingsContext.Provider>
  );
}

function useReaderSettings() {
  const context = useContext(ReaderSettingsContext);
  if (!context) throw new Error("ReadingControls must be inside ReaderPreferences");
  return context;
}

export function ReadingControls({ id }: { id?: string }) {
  const { fontSize, measure, setFontSize, setMeasure } = useReaderSettings();

  return (
    <div id={id} className="reading-controls">
      <fieldset>
        <legend>字体大小</legend>
        <div className="segmented-control">
          {([
            ["small", "小"],
            ["medium", "中"],
            ["large", "大"],
          ] as const).map(([value, label]) => (
            <label key={value} className={fontSize === value ? "selected" : undefined}>
              <input
                type="radio"
                name={`${id ?? "reader"}-font-size`}
                value={value}
                checked={fontSize === value}
                onChange={() => setFontSize(value)}
              />
              <span>{label}</span>
            </label>
          ))}
        </div>
      </fieldset>

      <fieldset>
        <legend>行宽</legend>
        <div className="segmented-control icon-segments">
          {([
            ["narrow", "窄行", TextAlignLeft],
            ["standard", "标准行宽", TextAlignCenter],
            ["wide", "宽行", TextAlignRight],
          ] as const).map(([value, label, Icon]) => (
            <label
              key={value}
              className={measure === value ? "selected" : undefined}
              title={label}
              aria-label={label}
            >
              <input
                type="radio"
                name={`${id ?? "reader"}-measure`}
                value={value}
                checked={measure === value}
                onChange={() => setMeasure(value)}
              />
              <span><Icon size={19} aria-label={label} /></span>
            </label>
          ))}
        </div>
      </fieldset>
    </div>
  );
}
