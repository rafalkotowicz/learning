public class LogLine {

    private final String logMessage;

    public LogLine(String logLine) {
        this.logMessage = logLine;
    }

    public LogLevel getLogLevel() {
        String logLevel = logMessage.substring(1, 4);
        return switch (logLevel) {
            case "TRC" -> LogLevel.TRACE;
            case "DBG" -> LogLevel.DEBUG;
            case "INF" -> LogLevel.INFO;
            case "WRN" -> LogLevel.WARNING;
            case "ERR" -> LogLevel.ERROR;
            case "FTL" -> LogLevel.FATAL;
            default -> LogLevel.UNKNOWN;
        };
    }

    public String getOutputForShortLog() {
        LogLevel logLevelToShorthen = getLogLevel();
        return this.logMessage.replaceFirst("\\[[A-Z]{3}]: ", logLevelToShorthen.getLogId().toString() + ":");
    }
}
