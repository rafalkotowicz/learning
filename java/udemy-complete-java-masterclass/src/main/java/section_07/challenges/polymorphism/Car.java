package section_07.challenges.polymorphism;

public class Car {
    private boolean engineStarted = false;
    private int wheels = 4;
    private double speed = 0;

    public int getWheels() {
        return wheels;
    }

    public double getSpeed() {
        return speed;
    }

    public String getName() {
        return name;
    }

    public int getCylinders() {
        return cylinders;
    }

    private String name;
    private int cylinders;

    public Car(int cylinders, String name) {
        this.name = name;
        this.wheels = 4;
        this.cylinders = cylinders;
    }

    public void startEngine() {
        this.engineStarted = true;
        
    }
    public void stopEngine()  {
        this.engineStarted = false;
    }
    public boolean isEngineRunning()  {
        return engineStarted;
    }
}
