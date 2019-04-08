package section_07.challenges;

public class Room {
    private Lamp standingLamp;
    private Lamp hangingLamp;
    private TV tv;

    public void turnOnLights() {
        standingLamp.turnOn();
        hangingLamp.turnOn();
    }

    public void turnOffLights() {
        standingLamp.turnOff();
        hangingLamp.turnOff();
    }
}
