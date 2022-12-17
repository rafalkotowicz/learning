public class LogLevels {

    public static String message(String logLine) {
        return logLine.replaceAll("\\[.*\\]: ", "").trim();
    }

    public static String logLevel(String logLine) {
        return logLine.replaceAll("\\[", "").replaceAll("\\]\\:", "").
                split(" ")[0].toLowerCase();
    }

    public static String reformat(String logLine) {
        return message(logLine) + " (" + logLevel(logLine) + ")";
    }
}
