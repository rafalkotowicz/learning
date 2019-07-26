import java.util.LinkedList;
import java.util.List;
import java.util.Map;

import static java.util.Map.entry;

class ProteinTranslator {

    Map<String, String> translation = Map.ofEntries(
            entry("AUG", "Methionine"),
            entry("UUU", "Phenylalanine"),
            entry("UUC", "Phenylalanine"),
            entry("UUA", "Leucine"),
            entry("UUG", "Leucine"),
            entry("UCU", "Serine"),
            entry("UCC", "Serine"),
            entry("UCA", "Serine"),
            entry("UCG", "Serine"),
            entry("UAU", "Tyrosine"),
            entry("UAC", "Tyrosine"),
            entry("UGU", "Cysteine"),
            entry("UGC", "Cysteine"),
            entry("UGG", "Tryptophan"),
            entry("UAA", "STOP"),
            entry("UAG", "STOP"),
            entry("UGA", "STOP"));

    List<String> translate(String rnaSequence) {
        List<String> proteins = new LinkedList<>();

        String protein = "";
        for (int i = 3; i <= rnaSequence.length(); i += 3) {
            switch (protein = translation.get(rnaSequence.substring(i - 3, i))) {
                case "STOP":
                    return proteins;
                default:
                    proteins.add(protein);
            }
        }
        return proteins;
    }
}