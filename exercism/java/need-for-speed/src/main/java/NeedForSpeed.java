class NeedForSpeed {
    private final int speed;
    private final int batteryDrain;
    private int batteryLevel;
    private int distanceDriven;

    public NeedForSpeed(int speed, int batteryDrain) {
        this.speed = speed;
        this.batteryDrain = batteryDrain;
        this.batteryLevel = 100;
    }

    public boolean batteryDrained() {
        return batteryDrain > batteryLevel;
    }

    public int distanceDriven() {
        return distanceDriven;
    }

    public void drive() {
        if (!batteryDrained()) {
            distanceDriven += speed;
            batteryLevel -= batteryDrain;
        }
    }

    public static NeedForSpeed nitro() {
        return new NeedForSpeed(50, 4);
    }
}

class RaceTrack {
    int trackLength;

    public RaceTrack(int trackLength) {
        this.trackLength = trackLength;
    }

    public boolean tryFinishTrack(NeedForSpeed car) {
        while (!car.batteryDrained()) {
            car.drive();
        }
        return trackLength <= car.distanceDriven();
    }
}
