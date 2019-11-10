package section_05

import org.junit.Test
import section_05.exercise.Week

class ListsTest {
    @Test
    void daysOfWeekTest() {
        def days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
        assert 7 == days.size()
    }

    @Test
    void removeMondayfromTheListTest() {
        def week = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
        assert week.contains(Week.MONDAY.toString())
        def weekWithoutMonday = week - Week.MONDAY.toString()
        assert !(weekWithoutMonday.contains(Week.MONDAY.toString()))
    }

    @Test
    void addingToListTest() {
        def weekPart1 = ["MONDAY", "TUESDAY", "WEDNESDAY"]
        def weekPart2 = ["THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
        def completeWeek = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
        assert completeWeek == weekPart1 + weekPart2
    }

    @Test
    void printingUsingIndexTest() {
        def completeWeek = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
        assert "MONDAY" == completeWeek[0]
        assert "SUNDAY" == completeWeek[6]
    }
}
