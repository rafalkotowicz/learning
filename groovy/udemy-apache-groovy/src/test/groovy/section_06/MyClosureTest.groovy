package section_06

import org.junit.Test

class MyClosureTest {

    @Test
    void summingClosureSums3ArgumentsTest() {
        assert 8 == MyClosure.summingClosure(1, 2, 5)
    }

    @Test
    void isDigitPositiveTest() {
        assert MyClosure.isDigit("1")
        List<String> toCheck = ["1", "222", "123123123"]
        Closure shouldBeTrue = { assert MyClosure.isDigit(it) }
        toCheck.forEach(shouldBeTrue)
    }

}
