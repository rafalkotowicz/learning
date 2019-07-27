package section_05.exercises;

public class FlourPacker {

    public static final int bigKilos = 5;

    public static boolean canPack(int bigCount, int smallCount, int goal) {
        if (bigCount < 0 || smallCount < 0 || goal < 0) {
            return false;
        }

        if ((bigCount * bigKilos + smallCount) >= goal && goal % bigKilos <= smallCount) {
            return true;
        } else {
            return false;
        }
    }
}
