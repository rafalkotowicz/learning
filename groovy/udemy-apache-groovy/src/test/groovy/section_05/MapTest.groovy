package section_05

import org.junit.Test

class MapTest {
    @Test
    void initializeAndCountElementsInMapTest() {
        def week = [
                1: "Monday",
                2: "Tuesday",
                3: "Wednesday",
                4: "Thursday",
                5: "Friday",
                6: "Saturday",
                7: "Sunday"
        ]
        assert "java.util.LinkedHashMap" == week.getClass().getName()
        assert 7 == week.size()
    }

    @Test
    void mapPrintoutTest() {
        def week = [
                1: "Monday",
                2: "Tuesday",
                3: "Wednesday",
                4: "Thursday",
                5: "Friday",
                6: "Saturday",
                7: "Sunday"
        ]
        assert "[Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]" == week.values().toString()
    }
}
