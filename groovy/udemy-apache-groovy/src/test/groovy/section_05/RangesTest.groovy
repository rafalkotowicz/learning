package section_05

import org.junit.Test
import section_05.exercise.Week

class RangesTest {
    @Test
    void weekHas7DaysTest() {
        assert 7 == Week.values().size()
    }

    @Test
    void weekRangeContainsAllDaysTest() {
        Range week = Week.MONDAY..Week.SUNDAY
        assert "[MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY]" == week.toListString()
        assert 7 == week.size()
    }

    @Test
    void wednesdayIsPartOfWeekTest() {
        Range week = Week.MONDAY..Week.SUNDAY
        assert week.contains(Week.WEDNESDAY)
    }

    @Test
    void canRetrieveFirstElementOfRangeTest() {
        Range week = Week.MONDAY..Week.SUNDAY
        assert Week.MONDAY == week.from
    }

    @Test
    void canRetrieveLastElementOfRangeTest() {
        Range week = Week.MONDAY..Week.SUNDAY
        assert Week.SUNDAY == week.to
    }
}
