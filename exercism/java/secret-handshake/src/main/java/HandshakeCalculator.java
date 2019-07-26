import java.util.Collections;
import java.util.LinkedList;
import java.util.List;

class HandshakeCalculator {
    List<Signal> calculateHandshake(int number) {
        List<Signal> secretHandshake = new LinkedList<Signal>();

        if (number % 32 == 0) {
            return secretHandshake;
        }

        String binary = Integer.toBinaryString(number);
        for (int i = 0; i < binary.length(); i++) {
            if (binary.charAt(binary.length() - i - 1) == '1') {
                switch (i) {
                    case (0):
                        secretHandshake.add(Signal.WINK);
                        break;
                    case (1):
                        secretHandshake.add(Signal.DOUBLE_BLINK);
                        break;
                    case (2):
                        secretHandshake.add(Signal.CLOSE_YOUR_EYES);
                        break;
                    case (3):
                        secretHandshake.add(Signal.JUMP);
                        break;
                    case (4):
                        Collections.reverse(secretHandshake);
                        break;
                }
            }
        }

        return secretHandshake;
    }
}
