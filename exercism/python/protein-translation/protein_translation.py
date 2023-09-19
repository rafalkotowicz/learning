def proteins(strand: str) -> [str]:
    mapping = {
        "AUG": "Methionine",
        "UUU": "Phenylalanine",
        "UUC": "Phenylalanine",
        "UUA": "Leucine",
        "UUG": "Leucine",
        "UCU": "Serine",
        "UCC": "Serine",
        "UCA": "Serine",
        "UCG": "Serine",
        "UAU": "Tyrosine",
        "UAC": "Tyrosine",
        "UGU": "Cysteine",
        "UGC": "Cysteine",
        "UGG": "Tryptophan",
        "UAA": "STOP",
        "UAG": "STOP",
        "UGA": "STOP"
    }

    codons: [str] = [strand[i:i + 3] for i in range(0, len(strand), 3)]
    proteins: [str] = []
    for codon in codons:
        protein: str = mapping[codon]
        if protein != "STOP":
            proteins.append(protein)
        else:
            break

    return proteins
