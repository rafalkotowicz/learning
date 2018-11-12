package section_02;

import java.util.Scanner;

public class HelloWorld {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Interacting with user is fun! Give a name, user.");
        String name = sc.nextLine();
        System.out.println("Hello, my name is " + name + ".");
    }
}
