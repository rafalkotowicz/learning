package section_05.exercises;

import org.junit.Assert;
import org.junit.Test;

public class PaintJobTest {
    @Test
    public void getBucketCount4PNegativeTest() {
        Assert.assertEquals("Expected invalid value (-1)", -1, PaintJob.getBucketCount(0, 0, 0, -1));
        Assert.assertEquals("Expected invalid value (-1)", -1, PaintJob.getBucketCount(0, 1, 1, 1));
        Assert.assertEquals("Expected invalid value (-1)", -1, PaintJob.getBucketCount(1, 0, 1, 1));
        Assert.assertEquals("Expected invalid value (-1)", -1, PaintJob.getBucketCount(1, 1, 0, 1));
        Assert.assertEquals("Expected invalid value (-1)", -1, PaintJob.getBucketCount(1, 1, 1, -1));
    }

    @Test
    public void getBucketCount4PNoBucketsAtHomeTest() {
        Assert.assertEquals(5, PaintJob.getBucketCount(3.4, 2.1, 1.5, 0));
        Assert.assertEquals(4, PaintJob.getBucketCount(2.75, 3.25, 2.5, 0));
    }

    @Test
    public void getBucketCount4PSomeBucketsAtHomeTest() {
        Assert.assertEquals(3, PaintJob.getBucketCount(3.4, 2.1, 1.5, 2));
        Assert.assertEquals(3, PaintJob.getBucketCount(2.75, 3.25, 2.5, 1));
    }

    @Test
    public void getBucketCount3PNegativeTest() {
        Assert.assertEquals("Expected invalid value (-1)", -1, PaintJob.getBucketCount(0, 0, 0));
        Assert.assertEquals("Expected invalid value (-1)", -1, PaintJob.getBucketCount(0, 0, 1));
        Assert.assertEquals("Expected invalid value (-1)", -1, PaintJob.getBucketCount(0, 1, 1));
        Assert.assertEquals("Expected invalid value (-1)", -1, PaintJob.getBucketCount(0, 1, 0));
        Assert.assertEquals("Expected invalid value (-1)", -1, PaintJob.getBucketCount(1, 1, 0));
        Assert.assertEquals("Expected invalid value (-1)", -1, PaintJob.getBucketCount(1, 0, 0));
    }

    @Test
    public void getBucketCount3PPositiveTest() {
        Assert.assertEquals(5, PaintJob.getBucketCount(3.4, 2.1, 1.5));
        Assert.assertEquals(4, PaintJob.getBucketCount(2.75, 3.25, 2.5));
        Assert.assertEquals(5, PaintJob.getBucketCount(3.4, 2.1, 1.5));
        Assert.assertEquals(14, PaintJob.getBucketCount(7.25, 4.3, 2.35));
    }

    @Test
    public void getBucketCount2PNegativeTest() {
        Assert.assertEquals("Expected invalid value (-1)", -1, PaintJob.getBucketCount(0, 0));
        Assert.assertEquals("Expected invalid value (-1)", -1, PaintJob.getBucketCount(0, 1));
        Assert.assertEquals("Expected invalid value (-1)", -1, PaintJob.getBucketCount(1, 0));
    }

    @Test
    public void getBucketCount2PPositiveTest() {
        Assert.assertEquals(3, PaintJob.getBucketCount(3.4, 1.5));
        Assert.assertEquals(3, PaintJob.getBucketCount(6.26, 2.2));
        Assert.assertEquals(5, PaintJob.getBucketCount(3.26, 0.75));
    }

}
