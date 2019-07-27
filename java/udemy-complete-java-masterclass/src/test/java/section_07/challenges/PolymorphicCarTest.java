package section_07.challenges;

import org.junit.Assert;
import org.junit.Test;
import section_07.challenges.polymorphism.AstonMartin;
import section_07.challenges.polymorphism.MitsubishiLancer;
import section_07.challenges.polymorphism.SkodaSuperb;

public class PolymorphicCarTest {
    @Test
    public void polymorphismTest() {
        AstonMartin am = new AstonMartin();
        MitsubishiLancer ml = new MitsubishiLancer();
        SkodaSuperb ss = new SkodaSuperb(4);

        Assert.assertEquals("Aston Martin DB9", am.getName());
        Assert.assertEquals("Mitsubishi Lancer", ml.getName());
        Assert.assertEquals("Skoda Superb", ss.getName());

        Assert.assertEquals("AstonMartin", am.getClass().getSimpleName());
    }
}
