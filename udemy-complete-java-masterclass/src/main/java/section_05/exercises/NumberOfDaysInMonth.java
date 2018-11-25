package section_05.exercises;

public class NumberOfDaysInMonth {
    public static boolean isLeapYear(int year) {
        if (year < 1 || year > 9_999) return false;
        return year % 400 == 0 || year % 4 == 0 && year % 100 != 0;
    }

    public static int getDaysInMonth(int month, int year) {
        if (year < 1 || year > 9_999) {
            return -1;
        }

        switch (month) {
            case 2:
                if(isLeapYear(year)) {
                    return 29;
                } else {
                    return 28;
                }
            case 4:
            case 6:
            case 9:
            case 11:
                return 30;
            case 1:
            case 3:
            case 5:
            case 7:
            case 8:
            case 10:
            case 12:
                return 31;
        }
        return -1;
    }
}
