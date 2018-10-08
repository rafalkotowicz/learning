package Chapter_02;

public class AppleRedAndHeavyPredicate implements ApplePredicate {
    public boolean test(Apple apple) {
        return "red".equals(apple.color) && apple.weight > 150;
    }
}
