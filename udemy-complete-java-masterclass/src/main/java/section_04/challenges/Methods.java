package section_04.challenges;

public class Methods {

    public static void displayHighScorePosition(String name, int position) {
        System.out.print(name + " managed to get into position " + position + " on the high score table");
    }

    public static int calculateHighScorePosition(int highScore) {
        if (highScore >= 1000) {
            return 1;
        } else if (highScore >= 500) {
            return 2;
        } else if (highScore >= 100) {
            return 3;
        }
        return 4;
    }
}
