export function toRna(dnaStrand: string) {
  const translations = new Map();
  translations.set("G", "C");
  translations.set("C", "G");
  translations.set("T", "A");
  translations.set("A", "U");

  // let rnaStrand: string[] = [];
  // for (let i = 0; i < dnaStrand.length; i++) {
  //   if (!translations.has(dnaStrand.at(i))) {
  //     throw new Error("Invalid input DNA.");
  //   }
  //   rnaStrand.push(translations.get(dnaStrand.at(i)));
  // }
  // return rnaStrand.join("");

  return [...dnaStrand].map(nucleotides => {
    if (!translations.has(nucleotides)) {
      throw new Error("Invalid input DNA.");
    }
    return translations.get(nucleotides);
  }).join("");
}