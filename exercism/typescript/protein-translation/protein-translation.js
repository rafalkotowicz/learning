export function translate(rnaSequence) {
    let rnaTranslation = new Map([
        ["AUG", "Methionine"],
        ["UUU", "Phenylalanine"],
        ["UUC", "Phenylalanine"],
        ["UUA", "Leucine"],
        ["UUG", "Leucine"],
        ["UCU", "Serine"],
        ["UCC", "Serine"],
        ["UCA", "Serine"],
        ["UCG", "Serine"],
        ["UAU", "Tyrosine"],
        ["UAC", "Tyrosine"],
        ["UGU", "Cysteine"],
        ["UGC", "Cysteine"],
        ["UGG", "Tryptophan"],
        ["UAA", "STOP"],
        ["UAG", "STOP"],
        ["UGA", "STOP"]
    ]);
    let proteins = [];
    let codonsBits = rnaSequence.split("");
    let codon = "";
    for (let codonBit of codonsBits) {
        if (codon.length < 3) {
            codon += codonBit;
        }
        else {
            codon = codonBit;
        }
        if (rnaTranslation.has(codon)) {
            if (rnaTranslation.get(codon) === "STOP") {
                break;
            }
            else {
                proteins.push(rnaTranslation.get(codon) ?? "");
            }
        }
    }
    return proteins;
}
