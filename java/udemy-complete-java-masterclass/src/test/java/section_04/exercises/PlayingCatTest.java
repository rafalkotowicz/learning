package section_04.exercises;

import org.junit.Test;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;
import static section_04.exercises.PlayingCat.isCatPlaying;

public class PlayingCatTest {
    @Test
    public void isCatPlayingTest() {
        assertFalse(isCatPlaying(true, 10));
        assertFalse(isCatPlaying(false, 36));
        assertTrue(isCatPlaying(false, 35));
        assertTrue(isCatPlaying(true, 33));

    }
}
