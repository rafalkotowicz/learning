package Chapter_02;

public class FancyFormatter implements AppleFormatter {
    public String accept(Apple a) {
        return "A " + (a.weight > 150 ? "heavy" : "light") + " " + a.color + " apple.";
    }
}

