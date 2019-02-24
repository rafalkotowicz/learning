package section_05.exercises;

public class DiagonalStar {
    public static void printSquareStar(int size) {
        if (size < 5) {
            System.out.print("Invalid Value");
            return;
        }

        for (int row = 1; row <= size; row++) {
            for (int col = 1; col <= size; col++) {
                if (row == 1 || row == size || col == 1 || col == size) { //borders
                    System.out.print("*");
                } else if (row == col) {
                    System.out.print("*");
                } else if (col == (size - row + 1)) {
                    System.out.print("*");
                } else {
                    System.out.print(" ");
                }
                if (col == size) System.out.print(System.lineSeparator());
            }
        }
    }
}
