export class Anagram {
    _word;
    constructor(input) {
        this._word = input.toLowerCase();
    }
    matches(...potentials) {
        let anagrams = [];
        let wordLetters = this._word.split("").sort();
        let isAnagram = true;
        for (let potential of potentials) {
            if (potential.toLowerCase() === this._word) {
                continue;
            }
            if (potential.length !== this._word.length) {
                continue;
            }
            let potentialLetters = potential.toLowerCase().split("").sort();
            for (let i = 0; i < wordLetters.length; i++) {
                if (wordLetters[i] !== potentialLetters[i]) {
                    isAnagram = false;
                    break;
                }
            }
            if (isAnagram) {
                anagrams.push(potential);
            }
            isAnagram = true;
        }
        return anagrams;
    }
}
