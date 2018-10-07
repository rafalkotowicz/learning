package Chapter_02;

public class ColorFormatter implements AppleFormatter {
    public String accept(Apple a) {
        return "A " + a.color + " apple.";
    }
}
