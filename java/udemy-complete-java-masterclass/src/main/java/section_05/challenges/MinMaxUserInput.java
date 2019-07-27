package section_05.challenges;

import java.util.Scanner;

public class MinMaxUserInput {

    public static void main(String... args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("I will tell you what is minimum and maximum value of values provided by you");

        int currentValue = 0;
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        while (scanner.hasNextInt()) {
            System.out.println("Provide next value.");
            currentValue = scanner.nextInt();
            if (currentValue < min) min = currentValue;
            if (currentValue > max) max = currentValue;
        }

        System.out.println("Your MAX is: " + max);
        System.out.println("Your MIN is: " + min);
        scanner.close();
    }
}
