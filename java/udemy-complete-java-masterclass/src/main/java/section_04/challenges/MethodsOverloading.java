package section_04.challenges;

public class MethodsOverloading {

    public static final int SECONDS_IN_MINUTE = 60;
    public static final int SECONDS_IN_HOUR = 3600;

    public static double calcImperialToMetric(double feet, double inches) {
        final int INCHES_IN_FEET = 12;
        if (feet < 0 || inches > 12 || inches < 0) {
            return -1d;
        }
        return calcImperialToMetric(feet * INCHES_IN_FEET + inches);
    }

    public static double calcImperialToMetric(double inches) {
        final double CMS_IN_INCH = 2.54;
        if (inches < 0) {
            return -1d;
        }
        return inches * CMS_IN_INCH;
    }

    public static String toHourMinutesSeconds(int seconds) {
        if (seconds < 0) {
            return "Invalid Parameter";
        }
        int hours = seconds / SECONDS_IN_HOUR;
        int minutes = (seconds - hours * SECONDS_IN_HOUR) / SECONDS_IN_MINUTE;
        int remainingSeconds = seconds % SECONDS_IN_MINUTE;


        return addLeadingZeroIfNecessary(hours) + "h " + addLeadingZeroIfNecessary(minutes) + "m " +
                addLeadingZeroIfNecessary(remainingSeconds) + "s";
    }

    public static String toHourMinutesSeconds(int minutes, int seconds) {
        if (minutes < 0) {
            return "Invalid Parameter - minutes";
        }
        if (seconds < 0 || seconds >= SECONDS_IN_MINUTE) {
            return "Invalid Parameter - seconds";
        }
        return toHourMinutesSeconds(minutes * SECONDS_IN_MINUTE + seconds);
    }

    private static String addLeadingZeroIfNecessary(int in) {
        return in < 10 ? "0" + in : "" + in;
    }
}
