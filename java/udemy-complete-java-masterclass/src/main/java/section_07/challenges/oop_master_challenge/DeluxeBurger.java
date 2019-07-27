package section_07.challenges.oop_master_challenge;

import java.util.Arrays;
import java.util.List;

public class DeluxeBurger extends Hamburger {
    public DeluxeBurger() {
        super("Deluxe Hamburger", BreadRoll.Deluxe, 15.00d, Arrays.asList(Additions.drink, Additions.fries), 2);
    }

    @Override
    public void addAddition(Additions additionalAddition) {
    }

    @Override
    public void addAdditions(List<Additions> additionalAdditions) {
    }

    @Override
    public void removeAddition(Additions addition) {
    }
}
