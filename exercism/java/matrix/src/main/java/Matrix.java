import java.security.InvalidParameterException;
import java.util.Arrays;
import java.util.Collections;
import java.util.LinkedList;

class Matrix {
    private LinkedList<LinkedList<Integer>> matrix;


    Matrix(String matrixAsString) {
        this.matrix = new LinkedList<>();
        LinkedList<Integer> row = new LinkedList<>();

        for(int position = 0; position < matrixAsString.length(); position++) {
            char currentChar = matrixAsString.charAt(position);

            if(Character.isDigit(currentChar)) {
                row.add(Character.getNumericValue(currentChar));
            }
            if(currentChar == ' ') {
                continue;
            }
            if(currentChar == '\n') {
                matrix.add(new LinkedList<>(row));
                row.clear();
            }
        }
        matrix.add(row);
    }

    int[] getRow(int rowNumber) {
        return Arrays.stream(matrix.get(rowNumber).toArray(new Integer[0])).mapToInt(Integer::intValue).toArray();
    }

    int[] getColumn(int columnNumber) {
        int[] requestedColumn = new int[matrix.size()];

        for(int row = 0; row < matrix.size(); row++) {
            requestedColumn[row] = matrix.get(row).get(columnNumber);
        }

        return requestedColumn;
    }

    int getRowsCount() {
        return matrix.size();
    }

    int getColumnsCount() {
        return matrix.getFirst().size();
    }
}
