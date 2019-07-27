package Chapter_02;

public class SimpleWeightFormatter implements AppleFormatter {
    public String accept(Apple a) {
        return "An apple weighting " + a.weight + " grams.";
    }
}

