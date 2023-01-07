public class ExperimentalRemoteControlCar implements RemoteControlCar {
    private int distanceTravelled = 0;

    public void drive() {
        throw new UnsupportedOperationException("Please implement the ExperimentalRemoteControlCar.drive() method");
    }

    @Override
    public void race(RemoteControlCar rcc) {
        distanceTravelled += 20;
    }

    @Override
    public int getDistanceTravelled() {
        return distanceTravelled;
    }
}
