package section_04.exercises;

import org.junit.Assert;
import org.junit.Test;

import static section_04.exercises.PlayingCat.*;

public class PlayingCatTest {
    @Test
    public void isCatPlayingTest() {
        Assert.assertFalse(isCatPlaying(true, 10));
        Assert.assertFalse(isCatPlaying(false, 36));
        Assert.assertTrue(isCatPlaying(false, 35));
        Assert.assertTrue(isCatPlaying(true, 33));

    }
}
