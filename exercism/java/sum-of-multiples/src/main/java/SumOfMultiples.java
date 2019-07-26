import java.util.HashSet;

class SumOfMultiples {
    private int upToNumber;
    private int[] multipleNumbers;

    SumOfMultiples(int number, int[] set) {
        upToNumber = number;
        multipleNumbers = set;
    }

    int getSum() {
        HashSet<Integer> multiples = new HashSet<>();
        for (int number = 0; number < upToNumber; number++) {
            for (Integer multipleNumber : multipleNumbers) {
                if (number % multipleNumber == 0) {
                    multiples.add(number);
                }
            }
        }

        int sumOfMultiples = 0;
        for (Integer multiple : multiples) {
            sumOfMultiples += multiple;
        }

        return sumOfMultiples;
    }

}
