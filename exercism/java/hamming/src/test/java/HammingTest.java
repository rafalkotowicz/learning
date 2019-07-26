import org.junit.Ignore;
import org.junit.Rule;
import org.junit.Test;
import org.junit.rules.ExpectedException;

import static org.junit.Assert.assertEquals;

public class HammingTest {

    @Rule
    public ExpectedException expectedException = ExpectedException.none();

    @Test
    public void testNoDistanceBetweenEmptyStrands() {
        assertEquals(0, new Hamming("", "").getHammingDifference());
    }

    @Test
    public void testNoDistanceBetweenShortIdenticalStrands() {
        assertEquals(0, new Hamming("A", "A").getHammingDifference());
    }

    @Test
    public void testNoDistanceBetweenLongIdenticalStrands() {
        assertEquals(0, new Hamming("GGACTGA", "GGACTGA").getHammingDifference());
    }

    @Test
    public void testCompleteDistanceInSingleNucleotideStrand() {
        assertEquals(1, new Hamming("A", "G").getHammingDifference());
    }

    @Test
    public void testCompleteDistanceInSmallStrand() {
        assertEquals(2, new Hamming("AG", "CT").getHammingDifference());
    }

    @Test
    public void testSmallDistanceInSmallStrand() {
        assertEquals(1, new Hamming("AT", "CT").getHammingDifference());
    }

    @Test
    public void testSmallDistanceInMediumStrand() {
        assertEquals(1, new Hamming("GGACG", "GGTCG").getHammingDifference());
    }

    @Test
    public void testSmallDistanceInLongStrand() {
        assertEquals(2, new Hamming("ACCAGGG", "ACTATGG").getHammingDifference());
    }

    @Test
    public void testNonUniqueCharacterInFirstStrand() {
        assertEquals(1, new Hamming("AGA", "AGG").getHammingDifference());
    }

    @Test
    public void testNonUniqueCharacterInSecondStrand() {
        assertEquals(1, new Hamming("AGG", "AGA").getHammingDifference());
    }

    @Test
    public void testSameNucleotidesInDifferentPositions() {
        assertEquals(2, new Hamming("TAG", "GAT").getHammingDifference());
    }

    @Test
    public void testLargeDistanceInPermutedStrand() {
        assertEquals(4, new Hamming("GATACA", "GCATAA").getHammingDifference());
    }

    @Test
    public void testLargeDistanceInOffByOneStrand() {
        assertEquals(9, new Hamming("GGACGGATTCTG", "AGGACGGATTCT").getHammingDifference());
    }

    @Test
    public void testValidatesFirstStrandNotLonger() {
        expectedException.expect(IllegalArgumentException.class);
        expectedException.expectMessage("leftStrand and rightStrand must be of equal length.");

        new Hamming("AATG", "AAA");
    }

    @Test
    public void testValidatesSecondStrandNotLonger() {
        expectedException.expect(IllegalArgumentException.class);
        expectedException.expectMessage("leftStrand and rightStrand must be of equal length.");

        new Hamming("ATA", "AGTG");
    }

}
