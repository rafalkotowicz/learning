import java.util.ArrayList;
import java.util.List;

class NaturalNumber {
    private int naturalNumber;

    public NaturalNumber(int number) {
        if (number <= 0) {
            throw new IllegalArgumentException("You must supply a natural number (positive integer)");
        }
        this.naturalNumber = number;
    }

    public Classification getClassification() {
        int aliquotSum = calculateAliquotSum(naturalNumber);
        if (aliquotSum == naturalNumber) {
            return Classification.PERFECT;
        } else if (aliquotSum < naturalNumber) {
            return Classification.DEFICIENT;
        } else {
            return Classification.ABUNDANT;
        }
    }

    private int calculateAliquotSum(int number) {
        int aliquotSum = 0;

        List<Integer> factors = findFactors(number);
        for (Integer factor : factors) {
            aliquotSum += factor;
        }

        return aliquotSum;
    }

    private List<Integer> findFactors(int number) {
        ArrayList<Integer> factors = new ArrayList<>();

        for (int i = 1; i <= number/2; i++) {
            if (number % i == 0) {
                factors.add(i);
            }
        }

        return factors;
    }
}
