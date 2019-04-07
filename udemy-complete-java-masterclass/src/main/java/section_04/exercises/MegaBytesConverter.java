package section_04.exercises;

public class MegaBytesConverter {

    public static void printMegaBytesAndKiloBytes(int kiloBytes) {
        if (kiloBytes < 0) {
            System.out.print("Invalid Value");
            return;
        }
        final int KILOS_IN_MEGA = 1024;
        final int megaBytes = kiloBytes / KILOS_IN_MEGA;
        final int remainingKilos = kiloBytes % KILOS_IN_MEGA;
        System.out.print(kiloBytes + " KB = " + megaBytes + " MB and " + remainingKilos + " KB");
    }
}
