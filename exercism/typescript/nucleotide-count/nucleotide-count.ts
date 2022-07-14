class Nucleotides {
  A: number;
  C: number;
  G: number;
  T: number;

  constructor() {
    this.A = 0;
    this.C = 0;
    this.G = 0;
    this.T = 0;
  }
}

export function nucleotideCounts(dnaSequence: string) {
  let result: Nucleotides = new Nucleotides();
  for (let i = 0; i < dnaSequence.length; i++) {
    switch (dnaSequence[i]) {
      case "A":
        result.A += 1;
        break;
      case "C":
        result.C += 1;
        break;
      case "G":
        result.G += 1;
        break;
      case "T":
        result.T += 1;
        break;
      default:
        throw new Error("Invalid nucleotide in strand");
    }
  }

  return result;
}
