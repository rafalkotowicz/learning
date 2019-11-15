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

    @Test
    void findAllTest1() {
        def items = [1, 2, 0, false, true, '', 'foo', [], [4, 5], null]
        assert items.findAll() == [1, 2, (true), 'foo', [4, 5]]
    }

    @Test
    void findAllTest2() {
        def items = [1, 2, 3, 4, 5, 6, 8, 11, 18]
        assert [3, 6, 18] == items.findAll(isDivisibleBy3)
    }

    @Test
    void anyAndEveryMethodTest() {
        List<Integer> testData = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        assert testData.any({ 0 == it % 3 })
        assert !testData.any({ it > 10 })
        assert testData.every({ it < 100 })
        assert !testData.every({ 0 == it % 2 })
    }

    @Test
    void groupByTest() {
        def result = [1, 2, 3, 4, 5, 6].groupBy({ it % 3 }, { it < 4 })
        assert result == [1: [(true): [1], (false): [4]], 2: [(true): [2], (false): [5]], 0: [(true): [3], (false): [6]]]
    }
}
