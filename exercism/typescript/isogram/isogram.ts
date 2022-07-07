export function isIsogram(word: string): boolean {
  let sanitizedWord = word.toLowerCase().replaceAll(new RegExp("[ \-]", "g"), "")
  let lettersSet = new Set(sanitizedWord.split(""));
  return lettersSet.size === sanitizedWord.length;
}