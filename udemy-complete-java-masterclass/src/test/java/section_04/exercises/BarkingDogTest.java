package section_04.exercises;

import org.junit.Assert;
import org.junit.Test;

import static section_04.exercises.BarkingDog.*;

public class BarkingDogTest {

    @Test
    public void barkTest() {
        Assert.assertTrue(bark(true, 1));
        Assert.assertFalse(bark(false, 2));
        Assert.assertFalse(bark(true, 8));
        Assert.assertFalse(bark(true, -1));
    }
}
