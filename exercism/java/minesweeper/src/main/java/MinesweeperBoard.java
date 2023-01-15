import java.util.ArrayList;
import java.util.List;

class MinesweeperBoard {
    private final List<String> board;
    private final int rows;
    private final int columns;

    public MinesweeperBoard(List<String> inputBoard) {
        board = new ArrayList<>();
        board.addAll(inputBoard);
        rows = inputBoard.size();
        columns = inputBoard.isEmpty() ? 0 : inputBoard.get(0).length();
    }

    public List<String> withNumbers() {
        applyMineCounters();
        return board;
    }

    private void applyMineCounters() {
        for (int y = 0; y < rows; y++) {
            for (int x = 0; x < columns; x++) {
                if (isMine(y, x)) {
                    continue;
                }
                int surroundingMinesFound = 0;
                //y-1, x-1
                if (checkYWithinBoard(y - 1) && checkXWithinBoard(x - 1) && isMine(y - 1, x - 1)) {
                    surroundingMinesFound += 1;
                }
                //y-1, x
                if (checkYWithinBoard(y - 1) && checkXWithinBoard(x) && isMine(y - 1, x)) {
                    surroundingMinesFound += 1;
                }
                //y-1, x+1
                if (checkYWithinBoard(y - 1) && checkXWithinBoard(x + 1) && isMine(y - 1, x + 1)) {
                    surroundingMinesFound += 1;
                }
                //y, x-1
                if (checkYWithinBoard(y) && checkXWithinBoard(x - 1) && isMine(y, x - 1)) {
                    surroundingMinesFound += 1;
                }
                //y, x+1
                if (checkYWithinBoard(y) && checkXWithinBoard(x + 1) && isMine(y, x + 1)) {
                    surroundingMinesFound += 1;
                }
                //y+1, x-1
                if (checkYWithinBoard(y + 1) && checkXWithinBoard(x - 1) && isMine(y + 1, x - 1)) {
                    surroundingMinesFound += 1;
                }
                //y+1, x
                if (checkYWithinBoard(y + 1) && checkXWithinBoard(x) && isMine(y + 1, x)) {
                    surroundingMinesFound += 1;
                }
                //y+1, x+1
                if (checkYWithinBoard(y + 1) && checkXWithinBoard(x + 1) && isMine(y + 1, x + 1)) {
                    surroundingMinesFound += 1;
                }
                if (surroundingMinesFound > 0) {
                    board.set(y, putMineCount(y, x, surroundingMinesFound));
                }
            }
        }
    }

    private String putMineCount(int y, int x, int mineCount) {
        String currentRow = board.get(y);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < columns; i++) {
            if (i != x) {
                sb.append(currentRow.charAt(i));
            } else {
                sb.append(mineCount);
            }
        }

        return sb.toString();
    }

    private boolean isMine(int y, int x) {
        return board.get(y).charAt(x) == '*';
    }

    private boolean checkYWithinBoard(int y) {
        return y >= 0 && y < rows;
    }

    private boolean checkXWithinBoard(int x) {
        return x >= 0 && x < columns;
    }
}