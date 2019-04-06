package section_06.exercises;

import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static utils.Constants.TOLERANCE;

public class ComplexNumberTest {
    @Test
    public void gettersTest() {
        ComplexNumber complexNumber = new ComplexNumber(1.2, 5.1);
        assertComplexNumberValue(complexNumber, 1.2, 5.1);
    }

    @Test
    public void addViaRealAndImaginaryPartProvisionTest() {
        ComplexNumber complexNumber = new ComplexNumber(1.2, 5.1);
        complexNumber.add(1.3, 4.9);
        assertComplexNumberValue(complexNumber, 2.5, 10.0);
    }

    @Test
    public void addTwoComplexNumbersObjectsTest() {
        ComplexNumber complexNumber1 = new ComplexNumber(1.1, 2.2);
        ComplexNumber complexNumber2 = new ComplexNumber(2.2, 3.3);
        complexNumber1.add(complexNumber2);
        assertComplexNumberValue(complexNumber1, 3.3, 5.5);
    }

    @Test
    public void subtractViaRealAndImaginaryPartProvisionTest() {
        ComplexNumber complexNumber = new ComplexNumber(1.2, 5.1);
        complexNumber.subtract(0.3, 4.9);
        assertComplexNumberValue(complexNumber, 0.9, 0.2);
    }

    @Test
    public void subtractComplexNumberByObjectTest() {
        ComplexNumber complexNumber1 = new ComplexNumber(1.1, 2.2);
        ComplexNumber complexNumber2 = new ComplexNumber(2.2, 3.3);
        complexNumber1.subtract(complexNumber2);
        assertComplexNumberValue(complexNumber1, -1.1, -1.1);
    }

    private void assertComplexNumberValue(ComplexNumber cn, double expectedReal, double expectedImaginary) {
        assertEquals(expectedReal, cn.getReal(), TOLERANCE);
        assertEquals(expectedImaginary, cn.getImaginary(), TOLERANCE);
    }
}
