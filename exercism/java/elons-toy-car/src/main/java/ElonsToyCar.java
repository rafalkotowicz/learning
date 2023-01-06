public class ElonsToyCar {
    private int batteryCharge;
    private int distanceTraveled;

    public ElonsToyCar() {
        this.batteryCharge = 100;
        this.distanceTraveled = 0;
    }

    public static ElonsToyCar buy() {
        return new ElonsToyCar();
    }

    public String distanceDisplay() {
        return String.format("Driven %s meters", this.distanceTraveled);
    }

    public String batteryDisplay() {
        return this.batteryCharge == 0 ? "Battery empty" : String.format("Battery at %s%%", this.batteryCharge);
    }

    public void drive() {
        int metersPerBatteryPercent = 20;
        int batteryDrainPerCycle = 1;

        if (this.batteryCharge > 0) {
            this.distanceTraveled += metersPerBatteryPercent;
            this.batteryCharge -= batteryDrainPerCycle;
        }
    }
}
