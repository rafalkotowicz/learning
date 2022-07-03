export function isPangram(sentence: string): boolean {
  const alphabet: Set<string> = new Set("abcdefghijklmnopqrstuvwxyz");
  for (let c of sentence) {
    alphabet.delete(c.toLowerCase());
  }
  return alphabet.size === 0
}
