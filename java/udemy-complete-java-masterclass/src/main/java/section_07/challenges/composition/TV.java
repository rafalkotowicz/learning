package section_07.challenges.composition;

public class TV {
    private boolean isTurnedOn;
    private int channel;

    public TV() {
        this.isTurnedOn = false;
        this.channel = 1;
    }

    public void turnOn() {
        this.isTurnedOn = true;
    }

    public void turnOff() {
        this.isTurnedOn = false;
    }

    public int getChannel() {
        return channel;
    }

    public void setChannel(int channel) {
        this.channel = channel;
    }
}
