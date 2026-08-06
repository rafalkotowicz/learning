class RectangleCounter {


    int countRectangles(String[] grid) {
        char[][] matrix = toCharGrid(grid);
        int rectangleCount = 0;

        for(int row = 0; row < matrix.length; row++) {
            for( int column = 0; column < matrix[row].length; column++) {
                if (matrix[row][column] == '+') {
                    for(int nextRow = row + 1; nextRow < matrix.length; nextRow++) {
                        if (matrix[nextRow][column] == '+') {
                            for(int nextColumn = column + 1; nextColumn < matrix[row].length; nextColumn++) {
                                if (matrix[row][nextColumn] == '+' && matrix[nextRow][nextColumn] == '+') {
                                    if (are4WalssPresent(matrix, row, column, nextRow, nextColumn)){
                                        rectangleCount++;
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }

        return rectangleCount;
    }

    private boolean are4WalssPresent(char[][] matrix, int row, int column, int nextRow, int nextColumn) {
        // TOP
        for (int currCol = column; currCol<=nextColumn; currCol++) {
            if (matrix[row][currCol] != '-' && matrix[row][currCol] != '+') {
                return false;
            }
        }

        // LEFT
        for (int currRow = row; currRow <= nextRow; currRow++) {
            if (matrix[currRow][column] != '|' && matrix[currRow][column] != '+') {
                return false;
            }
        }

        // RIGHT
        for (int currRow = row; currRow <= nextRow; currRow++) {
            if (matrix[currRow][nextColumn] != '|' && matrix[currRow][nextColumn] != '+') {
                return false;
            }
        }

        // BOTTOM
        for (int currCol = column; currCol <= nextColumn; currCol++) {
            if (matrix[nextRow][currCol] != '-' && matrix[nextRow][currCol] != '+') {
                return false;
            }
        }

        return true;
    }

    public static char[][] toCharGrid(String[] rows) {
        char[][] grid = new char[rows.length][];
        for (int i = 0; i < rows.length; i++) {
            grid[i] = rows[i].toCharArray();
        }
        return grid;
    }

}