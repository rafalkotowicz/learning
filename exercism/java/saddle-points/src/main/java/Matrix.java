import java.util.*;

class Matrix {
    private final List<List<Integer>> values;
    private final int rows;
    private int cols;

    Matrix(List<List<Integer>> values) {
        this.values = values;
        rows = values.size();
        if (rows > 0) {
            cols = values.get(0).size();
        }
    }

    Set<MatrixCoordinate> getSaddlePoints() {
        Set<MatrixCoordinate> foundSaddlePoints = new HashSet<>();
        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                if (isSaddlePoint(row, col)) {
                    foundSaddlePoints.add(new MatrixCoordinate(row + 1, col + 1));
                }
            }
        }
        return foundSaddlePoints;
    }

    private boolean isSaddlePoint(int row, int col) {
        int pointValue = values.get(row).get(col);
        List<Integer> rowValues = values.get(row);
        List<Integer> colValues = getColumnValues(col);

        return pointValue >= Collections.max(rowValues) && pointValue <= Collections.min(colValues);
    }

    private List<Integer> getColumnValues(int col) {
        List<Integer> colValues = new ArrayList<>();
        for (int row = 0; row < rows; row++) {
            colValues.add(values.get(row).get(col));
        }
        return colValues;
    }
}
