export function isIsogram(word) {
    let sanitizedWord = word.toLowerCase().replaceAll(new RegExp("[ \-]", "g"), "");
    let lettersSet = new Set(sanitizedWord.split(""));
    return lettersSet.size === sanitizedWord.length;
}
