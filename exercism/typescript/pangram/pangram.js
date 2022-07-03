export function isPangram(sentence) {
    const alphabet = new Set("abcdefghijklmnopqrstuvwxyz");
    for (let c of sentence) {
        alphabet.delete(c.toLowerCase());
    }
    return alphabet.size === 0;
}
