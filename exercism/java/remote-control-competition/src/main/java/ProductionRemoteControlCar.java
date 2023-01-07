class ProductionRemoteControlCar implements RemoteControlCar, Comparable {
    private int distanceTravelled = 0;
    private int numberofVictories = 0;

    public void drive() {
        throw new UnsupportedOperationException("Please implement the ProductionRemoteControlCar.drive() method");
    }

    public int getNumberOfVictories() {
        return numberofVictories;
    }

    public void setNumberOfVictories(int numberofVictories) {
        this.numberofVictories = numberofVictories;
    }

    @Override
    public void race(RemoteControlCar rcc) {
        distanceTravelled += 10;
    }

    @Override
    public int getDistanceTravelled() {
        return distanceTravelled;
    }

    @Override
    public int compareTo(Object o) {
        int thisVictories = this.getNumberOfVictories();
        int otherVictories = 0;
        if (o.getClass() == ProductionRemoteControlCar.class) {
            otherVictories = ((ProductionRemoteControlCar) o).getNumberOfVictories();
        }
        return thisVictories == otherVictories ? 0 : thisVictories > otherVictories ? 1 : -1;
    }
}
