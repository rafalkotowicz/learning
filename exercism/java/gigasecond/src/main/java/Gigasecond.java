import java.time.*;

class Gigasecond {
    private long gigasecond = 1_000_000_000L;
    private LocalDateTime birthDateTime;

    Gigasecond(LocalDate birthDate) {
        this.birthDateTime = LocalDateTime.of(birthDate, LocalTime.of(0,0,0));
    }

    Gigasecond(LocalDateTime birthDateTime) {
        this.birthDateTime = birthDateTime;
    }

    LocalDateTime getDate() {
        return birthDateTime.plusSeconds(gigasecond);
    }

}
