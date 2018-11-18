package section_03;

public class CharBoolean {
    public static int findUnicodePosition(char lookingFor) {
        for (int pos = 0; pos < Short.MAX_VALUE; pos++) {
            if ((char) (pos) == lookingFor) {
                return pos;
            }
        }
        return -1;
    }
}
