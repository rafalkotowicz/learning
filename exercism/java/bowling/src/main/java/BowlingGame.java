import java.util.ArrayList;
import java.util.List;

class BowlingGame {
    static int STRIKE = 10;
    static int SPARE = 10;
    List<Integer> rolls;

    BowlingGame() {
        rolls = new ArrayList<Integer>();
    }

    public void roll(int pins) {
        if (pins < 0) {
            throw new IllegalStateException("Negative roll is invalid");
        }
        if (pins > STRIKE) {
            throw new IllegalStateException("Pin count exceeds pins on the lane");
        }
        int previousRoll = rolls.size() > 0 ? rolls.get(rolls.size() - 1) : 0;
        if (previousRoll < STRIKE && previousRoll + pins > STRIKE) {
            throw new IllegalStateException("Pin count exceeds pins on the lane");
        }
        rolls.add(pins);
    }

    public int score() {
        int frame = 1;
        int sum = 0;
        for (int i = 0; i < rolls.size(); i += 2) {
            int currRoll = rolls.get(i);
            int nextRoll = i + 1 < rolls.size() ? rolls.get(i + 1) : 0;
            int nextNextRoll = i + 2 < rolls.size() ? rolls.get(i + 2) : 0;

            if (frame < 10) {
                if (currRoll == STRIKE) {
                    sum += currRoll + nextRoll + nextNextRoll;
                    i -= 1;
                } else if (currRoll + nextRoll == SPARE) {
                    sum += currRoll + nextRoll + nextNextRoll;
                } else {
                    sum += currRoll + nextRoll;
                }
            } else {
                sum += currRoll + nextRoll + nextNextRoll;
                break;
            }
            frame += 1;
        }
        System.out.println(frame);
        return sum;
    }
}