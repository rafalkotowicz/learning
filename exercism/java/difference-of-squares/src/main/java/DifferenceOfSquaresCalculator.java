import java.util.stream.IntStream;

public class DifferenceOfSquaresCalculator {
    int computeSquareOfSumTo(int upTo) {
        return (int)Math.pow(IntStream.range(1, upTo + 1).sum(), 2);
    }

    int computeSumOfSquaresTo(int upTo) {
        return IntStream.range(1, upTo + 1).map(a -> (int)Math.pow(a, 2)).sum();
    }

    int computeDifferenceOfSquares(int upTo) {
        return computeSquareOfSumTo(upTo) - computeSumOfSquaresTo(upTo);
    }
}
