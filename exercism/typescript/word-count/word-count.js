export function count(phrase) {
    let result = new Map();
    let words = phrase.trim().split(new RegExp("[ \\t\\n][ ]*"));
    let wordsLower = words.map(x => x.toLowerCase());
    for (let word of wordsLower) {
        if (result.has(word)) {
            // @ts-ignore
            result.set(word, result.get(word) + 1);
        }
        else {
            result.set(word, 1);
        }
    }
    return result;
}
