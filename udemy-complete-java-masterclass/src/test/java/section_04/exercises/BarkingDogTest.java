package section_04.exercises;

import org.junit.Assert;
import org.junit.Test;

public class BarkingDogTest {

    @Test
    public void barkTest() {
        Assert.assertTrue(BarkingDog.bark(true, 1));
        Assert.assertFalse(BarkingDog.bark(false, 2));
        Assert.assertFalse(BarkingDog.bark(true, 8));
        Assert.assertFalse(BarkingDog.bark(true, -1));
    }
}
