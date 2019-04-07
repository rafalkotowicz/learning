package section_05.exercises;

import java.util.Scanner;

public class InputCalculator {
    public static void main(String... args) {
        //public static void inputThenPrintSumAndAverage() {

        Scanner scanner = new Scanner(System.in);

        int sum = 0;
        int inputCounter = 0;
        while (scanner.hasNextInt()) {
            sum += scanner.nextInt();
            inputCounter += 1;

        }

        System.out.println("SUM = " + sum + " AVG = " + Math.round((double) sum / inputCounter));
        scanner.close();
    }
}
