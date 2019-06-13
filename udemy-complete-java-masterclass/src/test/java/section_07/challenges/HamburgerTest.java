package section_07.challenges;

import org.junit.Test;
import section_07.challenges.oop_master_challenge.Additions;
import section_07.challenges.oop_master_challenge.DeluxeBurger;
import section_07.challenges.oop_master_challenge.Hamburger;
import section_07.challenges.oop_master_challenge.HealthyBurger;

import java.util.Arrays;

import static org.junit.Assert.assertEquals;
import static section_07.challenges.oop_master_challenge.Additions.*;
import static section_07.challenges.oop_master_challenge.BreadRoll.BrownRye;
import static section_07.challenges.oop_master_challenge.BreadRoll.Wheat;
import static utils.Constants.TOLERANCE;

public class HamburgerTest {
    @Test
    public void HamburgerCanBeCreatedTest() {
        Hamburger hamburger = new Hamburger("hamburgerName", Wheat, 7.00);
        assertEquals("hamburgerName", hamburger.getName());
        assertEquals(7.00, hamburger.getBasePrice(), TOLERANCE);
        assertEquals("Wheat", hamburger.getBreadRoll().getName());
    }

    @Test
    public void HamburgerCanHaveAdditionsTest() {
        Hamburger hamburger = new Hamburger("hamburgerName", Wheat, 7.00, 10);
        assertEquals("There should be no additions", 0, hamburger.getAdditions().size());
        hamburger.addAddition(tomato);
        assertEquals("There should be 1 addition", 1, hamburger.getAdditions().size());
        hamburger.addAddition(tomato);
        hamburger.addAddition(Additions.lettuce);
        assertEquals("There should be 3 additions", 3, hamburger.getAdditions().size());
        hamburger.removeAddition(tomato);
        assertEquals("There should be 2 additions", 2, hamburger.getAdditions().size());
    }

    @Test
    public void HealthyBurgerIsBrownRyeTest() {
        HealthyBurger healthyBurger = new HealthyBurger("Healthy Burger", 10.0);
        assertEquals(BrownRye, healthyBurger.getBreadRoll());
    }

    @Test
    public void HealthyBurgerCanHaveMaximumOf6AdditionsTest() {
        HealthyBurger healthyBurger = new HealthyBurger("Healthy Burger", 10.0);
        healthyBurger.addAdditions(Arrays.asList(tomato, lettuce, onion, friedOnion, sesame, cashewNuts));
        assertEquals("There should be 6 additions", 6, healthyBurger.getAdditions().size());
        healthyBurger.addAddition(drink);
        assertEquals("There should be 6 additions", 6, healthyBurger.getAdditions().size());
        healthyBurger.addAdditions(Arrays.asList(tomato, lettuce, onion, friedOnion, sesame, cashewNuts));
        assertEquals("There should be 6 additions", 6, healthyBurger.getAdditions().size());
    }

    @Test
    public void DeluxeBurgerHas2FixedAdditionsTest() {
        DeluxeBurger deluxeBurger = new DeluxeBurger();
        assertEquals("Deluxe Burger has exactly 2 additions", 2, deluxeBurger.getAdditions().size());
        assertEquals("And this additions are: drink & fries", deluxeBurger.getAdditions(), Arrays.asList(Additions.drink, Additions.fries));
        deluxeBurger.addAddition(friedOnion);
        assertEquals("Cannot add more than 2 additions", 2, deluxeBurger.getAdditions().size());
        deluxeBurger.addAdditions(Arrays.asList(friedOnion, tomato));
        assertEquals("Cannot add more than 2 additions", 2, deluxeBurger.getAdditions().size());
        deluxeBurger.removeAddition(drink);
        assertEquals("Cannot remove additions", 2, deluxeBurger.getAdditions().size());
    }

    @Test
    public void getTotalPriceOfABurgerTest() {
        Hamburger basicHamburger = new Hamburger("Basic Burger", Wheat, 8.00d, 4);
        assertEquals(8.00, basicHamburger.getTotalPrice(), TOLERANCE);
        basicHamburger.addAddition(drink);
        assertEquals(10.50, basicHamburger.getTotalPrice(), TOLERANCE);

        HealthyBurger healthyBurger = new HealthyBurger("Dorito Burger", 10);
        assertEquals(10.00, healthyBurger.getTotalPrice(), TOLERANCE);
        healthyBurger.addAdditions(Arrays.asList(tomato, lettuce, onion, friedOnion, sesame, cashewNuts));
        assertEquals(18.40, healthyBurger.getTotalPrice(), TOLERANCE);

        DeluxeBurger deluxeBurger = new DeluxeBurger();
        assertEquals(20.50, deluxeBurger.getTotalPrice(), TOLERANCE);
    }

    @Test
    public void printBillTest() {
        String expectedBillPrintout = "~~~ Bills Burgers ~~~\n" +
                "Burger: Basic Burger\n" +
                "Bread: Wheat\n" +
                "Additions: NONE\n" +
                "Total price: 8,00$";
        Hamburger basicHamburger = new Hamburger("Basic Burger", Wheat, 8.00, 4);
        assertEquals(expectedBillPrintout, basicHamburger.getBill());

        basicHamburger.addAdditions(Arrays.asList(tomato, lettuce));
        String expectedBillPrintout2 = "~~~ Bills Burgers ~~~\n" +
                "Burger: Basic Burger\n" +
                "Bread: Wheat\n" +
                "Additions: \n" +
                "  - Tomato\n" +
                "  - Lettuce\n" +
                "Total price: 8,80$";
        assertEquals(expectedBillPrintout2, basicHamburger.getBill());
    }

}
