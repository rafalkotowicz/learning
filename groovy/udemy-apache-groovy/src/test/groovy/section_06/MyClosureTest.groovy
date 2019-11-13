package section_06

import org.junit.Test

import static section_06.MyClosure.*

class MyClosureTest {

    @Test
    void summingClosureTest() {
        assert 8 == summingClosure(1, 2, 5)
        assert 3 == summingClosure(1, 2)
        assert 4 == summingClosure(0, 4)
        assert 3 == summingClosure(-1, 4)
        assert -1 == summingClosure(-1)
    }

    @Test
    void isDigitPositiveTest() {
        List<String> toCheck = ["1", "222", "123123123"]
        toCheck.forEach({ assert isNumber(it) })
    }

    @Test
    void applyClosureToMapTest() {
        def testData = [surname: "Denis", familyname: "Rodman"]
        testData.forEach({ def key, def value ->
            assert printMap(key, value).matches(".*name:.*")
        })
    }

    @Test
    void curryTest() {
        assert 20.0 == calculatePaintPrice.call(10.0, 2.0, 4.0)
        assert 20.0 == calculatePaintPriceFixedArea(2.0, 4.0)
        assert 20.0 == calculatePaintPriceFixedPrice(10.0, 2.0)
    }
}
