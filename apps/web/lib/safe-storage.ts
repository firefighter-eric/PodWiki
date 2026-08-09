type StorageLike = Pick<Storage, "getItem" | "setItem">;

const memoryFallback = new Map<string, string>();

function getBrowserLocalStorage(): StorageLike | undefined {
  try {
    return typeof window === "undefined" ? undefined : window.localStorage;
  } catch {
    return undefined;
  }
}

export function readLocalStorage(
  key: string,
  fallback: string,
  storage: StorageLike | undefined = getBrowserLocalStorage(),
): string {
  try {
    return storage?.getItem(key) ?? memoryFallback.get(key) ?? fallback;
  } catch {
    return memoryFallback.get(key) ?? fallback;
  }
}

export function writeLocalStorage(
  key: string,
  value: string,
  storage: StorageLike | undefined = getBrowserLocalStorage(),
): boolean {
  memoryFallback.set(key, value);
  try {
    storage?.setItem(key, value);
    return storage !== undefined;
  } catch {
    return false;
  }
}

export function clearLocalStorageFallbackForTests() {
  memoryFallback.clear();
}
