import java.util.function.DoublePredicate;

class Leap {

    boolean isLeapYear(int year) {
        DoublePredicate divisibleBy4 = x -> x % 4 == 0;
        DoublePredicate divisibleBy100 = x -> x % 100 == 0;
        DoublePredicate divisibleBy400 = x -> x % 400 == 0;

        if (divisibleBy400.test(year)) {
            return true;
        } else if (divisibleBy100.test(year)) {
            return false;
        } else return divisibleBy4.test(year);
    }
}
