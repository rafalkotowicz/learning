package section_04.exercises;

public class MinutesToYearsDaysCalculator {
    public static void printYearsAndDays(long minutes) {
        if (minutes < 0) {
            System.out.print("Invalid Value");
            return;
        }
        final int minutesInHour = 60;
        final int hoursInDay = 24;
        final int daysInYear = 365;
        long days = minutes / (hoursInDay * minutesInHour);
        long years = days / daysInYear;
        days = days - years * daysInYear;
        System.out.print(minutes + " min = " + years + " y and " + days + " d");
    }
}
