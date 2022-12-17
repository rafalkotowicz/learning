public class Lasagna {
    public int expectedMinutesInOven() {
        return 40;
    }

    public int remainingMinutesInOven(int alreadyInOven) {
        return 40 - alreadyInOven;
    }

    public int preparationTimeInMinutes(int noOfLayers) {
        return noOfLayers * 2;
    }

    public int totalTimeInMinutes(int noOfLayers, int timeInOven) {
        return preparationTimeInMinutes(noOfLayers) + timeInOven;
    }
}
