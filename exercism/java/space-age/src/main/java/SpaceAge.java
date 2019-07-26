class SpaceAge {
    enum SolarSystem {
        MERCURY(0.2408467f),
        VENUS(0.61519726f),
        EARTH(1),
        MARS(1.8808158f),
        JUPITER(11.862615f),
        SATURN(29.447498f),
        URANUS(84.016846f),
        NEPTUNE(164.79132f);

        private static int EARTH_YEAR_IN_SECONDS = 31557600;
        private final double orbitalPeriodInEarthYears;

        SolarSystem(double earthYears) {
            this.orbitalPeriodInEarthYears = earthYears;
        }

        double localAge(long seconds) {
            return (double) seconds /EARTH_YEAR_IN_SECONDS / orbitalPeriodInEarthYears;
        }
    }

    private long secondsOnEarth;

    SpaceAge(long seconds) {
        this.secondsOnEarth = seconds;
    }

    long getSeconds() {
        return secondsOnEarth;
    }

    double onEarth() {
        return SolarSystem.EARTH.localAge(secondsOnEarth);
    }

    double onMercury() {
        return SolarSystem.MERCURY.localAge(secondsOnEarth);
    }

    double onVenus() {
        return SolarSystem.VENUS.localAge(secondsOnEarth);
    }

    double onMars() {
        return SolarSystem.MARS.localAge(secondsOnEarth);
    }

    double onJupiter() { return SolarSystem.JUPITER.localAge(secondsOnEarth); }

    double onSaturn() {
        return SolarSystem.SATURN.localAge(secondsOnEarth);
    }

    double onUranus() {
        return SolarSystem.URANUS.localAge(secondsOnEarth);
    }

    double onNeptune() { return SolarSystem.NEPTUNE.localAge(secondsOnEarth); }
}
