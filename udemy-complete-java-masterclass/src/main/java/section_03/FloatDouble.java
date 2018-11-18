package section_03;

public class FloatDouble {
    private static double POUND_IN_KILOS = 0.453_592_37d;

    public static double poundToKiloConverter(double pounds) {
        return pounds * POUND_IN_KILOS;
    }
}
