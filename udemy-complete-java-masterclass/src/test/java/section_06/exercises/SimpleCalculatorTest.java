package section_06.exercises;

import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

/*
Write a class with the name SimpleCalculator. The class needs two fields (instance variables) with names firstNumber and secondNumber both of type double.

Write the following methods (instance methods):

*Method named getFirstNumber without any parameters, it needs to return the value of firstNumber field.
*Method named getSecondNumber without any parameters, it needs to return the value of secondNumber field.
*Method named setFirstNumber with one parameter of type double, it needs to set the value of the firstNumber field.
*Method named setSecondNumber with one parameter of type double, it needs to set the value of the secondNumberfield.
*Method named getAdditionResult without any parameters, it needs to return the result of adding the field values of firstNumber and secondNumber.
*Method named getSubtractionResult without any parameters, it needs to return the result of subtracting the field values of secondNumber from the firstNumber.
*Method named getMultiplicationResult without any parameters, it needs to return the result of multiplying the field values of firstNumber and secondNumber.
*Method named getDivisionResult without any parameters it needs to return the result of dividing the field values of firstNumber by the secondNumber. In case the value of secondNumber is 0 then return 0.

TEST EXAMPLE

TEST CODE:

SimpleCalculator calculator = new SimpleCalculator();
calculator.setFirstNumber(5.0);
calculator.setSecondNumber(4);
System.out.println("add= " + calculator.getAdditionResult());
System.out.println("subtract= " + calculator.getSubtractionResult());
calculator.setFirstNumber(5.25);
calculator.setSecondNumber(0);
System.out.println("multiply= " + calculator.getMultiplicationResult());
System.out.println("divide= " + calculator.getDivisionResult());

OUTPUT

add= 9.0
subtract= 1.0
multiply= 0.0
divide= 0.0

TIPS:

*add= 9.0 is printed because 5.0 + 4 is 9.0
*subtract= 1.0 is printed because 5.0 - 4 is 1.0
*multiply= 0.0 is printed because 5.25 * 0 is 0.0
*divide= 0.0 is printed because secondNumber is set to 0


NOTE: All methods should be defined as public NOT public static.

NOTE: In total, you have to write 8 methods.

NOTE: Do not add the main method to the solution code.
 */
public class SimpleCalculatorTest {
    private SimpleCalculator simpleCalculator;
    private double TOLERATION = 0.00000001;

    @Before
    public void initializeTestData() {
        simpleCalculator = new SimpleCalculator();
        simpleCalculator.setFirstNumber(4);
        simpleCalculator.setSecondNumber(2);
    }

    @Test
    public void getAdditionResultPositiveTest() {
        Assert.assertEquals(6.0, simpleCalculator.getAdditionResult(), TOLERATION);
    }

    @Test
    public void getSubtractionResultPositiveTest() {
        Assert.assertEquals(2.0, simpleCalculator.getSubtractionResult(), TOLERATION);
    }

    @Test
    public void getMultiplicationResultPositiveTest() {
        Assert.assertEquals(8.0, simpleCalculator.getMultiplicationResult(), TOLERATION);
    }

    @Test
    public void getDivisionResultPositiveTest() {
        Assert.assertEquals(2.0, simpleCalculator.getDivisionResult(), TOLERATION);
    }

    @Test
    public void getDivisionResultDivisionByZeroTest() {
        simpleCalculator.setSecondNumber(0);
        Assert.assertEquals(0.0, simpleCalculator.getDivisionResult(), TOLERATION);
    }
}
