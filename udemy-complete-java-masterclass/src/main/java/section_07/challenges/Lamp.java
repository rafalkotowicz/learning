package section_07.challenges;

public class Lamp {
    private boolean isTurnedOn;

    public Lamp() {
        this.isTurnedOn = false;
    }

    void turnOn() {
        this.isTurnedOn = true;
    }

    void turnOff() {
        this.isTurnedOn = false;
    }

    public boolean isTurnedOn() {
        return isTurnedOn;
    }
}
