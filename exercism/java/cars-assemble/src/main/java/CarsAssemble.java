public class CarsAssemble {
    private static int CARS_PER_HOUR = 221;

    public double productionRatePerHour(int speed) {
        double productionRate = CARS_PER_HOUR * speed;
        double successRate = 0.0d;
        if (speed <= 4) {
            successRate = 1;
        } else if (speed <= 8) {
            successRate = 0.9;
        } else if (speed == 9) {
            successRate = 0.8;
        } else if (speed == 10) {
            successRate = 0.77;
        } else {
            throw new IllegalArgumentException("Speed must be in range [1, 10]");
        }

        return productionRate * successRate;
    }

    public int workingItemsPerMinute(int speed) {
        return (int) Math.floor(productionRatePerHour(speed) / 60);
    }
}
