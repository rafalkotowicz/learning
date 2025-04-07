export function parse(phrase: string): string {
  // Iteration 1
  // let words: string[] | string[][] = phrase.split(new RegExp("[ \-]"))
  //
  // let letters: string[] = [];
  // let newWord: string = "";
  // let newWords: string[] = [];
  // let previousLetter: string = "";
  // for (let i = 0; i < words.length; i++) {
  //   letters = words[i].split("");
  //   //HyperText
  //   for (let j = 0; j < letters.length; j++) {
  //     if (previousLetter.match(new RegExp("[a-z]")) &&
  //       letters[j].match(new RegExp("[A-Z]"))) {
  //       newWords.push(newWord);
  //       newWord = letters[j]
  //     } else {
  //       newWord += letters[j]
  //     }
  //     previousLetter = letters[j];
  //   }
  //   newWords.push(newWord);
  //   newWord = "";
  //   previousLetter = "";
  // }
  //
  // return newWords.map(x => x[0].toUpperCase()).reduce((x, y) => x + y)

  // Iteration 2 : Better regex finding words
  let words: string[] = phrase.match(/[A-Z]+[a-z]*|[a-z]+/g) || [];
  return words.map(x => x[0].toUpperCase()).reduce((x, y) => x + y)
}