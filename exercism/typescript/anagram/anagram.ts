export class Anagram {
  _word: string

  constructor(input: string) {
    this._word = input.toLowerCase();
  }

  public matches(...potentials: string[]): string[] {
    let anagrams: string[] = [];
    let wordLetters: string[] = this._word.split("").sort();
    let isAnagram: boolean = true;
    for (let potential of potentials) {
      if (potential.toLowerCase() === this._word) {
        continue;
      }
      if (potential.length !== this._word.length) {
        continue;
      }
      let potentialLetters: string[] = potential.toLowerCase().split("").sort();
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
