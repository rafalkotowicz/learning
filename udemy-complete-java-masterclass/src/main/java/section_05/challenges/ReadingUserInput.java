package section_05.challenges;

import java.util.Scanner;

public class ReadingUserInput {

    public static void main(String... args) {
        Scanner scanner = new Scanner(System.in);

        int sum = 0;
        for (int i = 1; i <= 10; i++) {
            System.out.println("Enter number #" + i + ":");
            if(scanner.hasNextInt()) {
                sum += scanner.nextInt();
            } else {
                System.out.println("Provided input is not a number");
                scanner.nextLine();
            }
        }

        System.out.println("User provided integers that amounts to: " + sum);
        scanner.close();
    }
}
