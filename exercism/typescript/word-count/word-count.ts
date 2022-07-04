export function count(phrase: string): Map<string | number, number> {
  let result: Map<string | number, number> = new Map<string | number, number>()

  let words: string[] = phrase.trim().split(new RegExp("[ \\t\\n][ ]*"));
  let wordsLower: string[] = words.map(x => x.toLowerCase());

  for (let word of wordsLower) {
    if (result.has(word)) {
      // @ts-ignore
      result.set(word, result.get(word) + 1);
    } else {
      result.set(word, 1);
    }
  }

  return result;
}
