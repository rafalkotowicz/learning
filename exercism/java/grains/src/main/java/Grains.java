import java.math.BigInteger;
import java.util.stream.IntStream;

class Grains {

    private void validateInput(final int square) {
        if (square < 1 || square > 64) {
            throw new IllegalArgumentException("square must be between 1 and 64");
        }
    }

    BigInteger grainsOnSquare(final int square) {
        validateInput(square);
        return BigInteger.TWO.pow(square - 1);
    }

    BigInteger grainsOnBoard() {
        return IntStream.range(1, 65).mapToObj(x -> grainsOnSquare(x)).reduce(BigInteger.ZERO, BigInteger::add);
    }

}
