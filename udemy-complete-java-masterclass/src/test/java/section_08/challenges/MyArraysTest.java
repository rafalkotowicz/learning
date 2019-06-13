package section_08.challenges;

import org.junit.Assert;
import org.junit.Test;

public class MyArraysTest {
    @Test
    public void sortDescendingArrayTest() {
        int[] input = {4, 3, 6, 22, 33, 11};
        int[] expectedOutput = {33, 22, 11, 6, 4, 3};

        Assert.assertArrayEquals(expectedOutput, MyArrays.reverseSort(input));
    }
}
