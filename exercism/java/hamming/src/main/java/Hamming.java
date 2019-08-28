import java.security.InvalidParameterException;

public class Hamming {
    private String leftStrand;
    private String rightStrand;

    Hamming(String leftStrand, String rightStrand) {
        if (leftStrand.length() != rightStrand.length()) {
            throw new IllegalArgumentException("leftStrand and rightStrand must be of equal length.");
        }

        this.leftStrand = leftStrand;
        this.rightStrand = rightStrand;
    }

    int getHammingDifference() {
        int difference = 0;
        for (int i = 0; i < leftStrand.length(); i++) {
            if (leftStrand.charAt(i) != rightStrand.charAt(i)) {
                difference++;
            }
        }

        return difference;
    }

}