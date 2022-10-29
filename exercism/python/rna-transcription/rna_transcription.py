DNA_NUCLEOTIDES = "GCTA"
RNA_NUCLEOTIDES = "CGAU"
DNA_RNA_TRANSCRIBE = str.maketrans(DNA_NUCLEOTIDES, RNA_NUCLEOTIDES)


def to_rna(dna_strand: str) -> str:
    """Translates DNA sequence into RNA sequence.
    :param dna_strand: str - DNA sequence to translate
    :return: str - RNA sequence or empty string if any DNA element won't be recognized
    """
    if any(nucleotide not in DNA_NUCLEOTIDES for nucleotide in dna_strand):
        return ""
    return dna_strand.translate(DNA_RNA_TRANSCRIBE)
