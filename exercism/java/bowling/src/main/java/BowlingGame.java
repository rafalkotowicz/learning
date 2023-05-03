/*

Since this exercise has a difficulty of > 4 it doesn't come
with any starter implementation.
This is so that you get to practice creating classes and methods
which is an important part of programming in Java.

Please remove this comment when submitting your solution.

*/


import java.util.ArrayList;
import java.util.logging.Logger;


class Frame {
    public int id;
    public ArrayList<Integer> rolls;

    public Frame(int id) {
        this.id = id;
        this.rolls = new ArrayList<>();
    }

    public boolean isFrameFull() {
        return !is10thFrame() && (getSumOfRolls() >= 10 || rolls.size() == 2);
    }

    protected int getSumOfRolls() {
        return rolls.stream().reduce(0, (x, y) -> x + y);
    }

    public boolean isSpare() {
        return !is10thFrame() && getSumOfRolls() == 10 && rolls.size() == 2;
    }

    public boolean isStrike() {
        return !is10thFrame() && getSumOfRolls() == 10 && rolls.size() == 1;
    }

    public boolean is10thFrame() {
        return id == 9;
    }

    public boolean is10thFrameCompleted() {
        if (is10thFrame() && rolls.size() == 2 && getSumOfRolls() < 10) {
            return true;
        } else return is10thFrame() && rolls.size() == 3;
    }

    public boolean isFillBallNeeded() {
        int maybe1 = rolls.size() >= 1 ? rolls.get(0) : 0;
        int maybe2 = rolls.size() >= 2 ? rolls.get(1) : 0;

        return is10thFrame() && maybe1 + maybe2 >= 10;
    }
}

public class BowlingGame {
    private final static int MIN_PINS = 0;
    private final static int MAX_PINS = 10;
    private final ArrayList<Frame> frames;
    private final Logger logger = Logger.getLogger(BowlingGame.class.getName());
    private Frame currentFrame;

    public BowlingGame() {
        this.frames = new ArrayList<Frame>();
        initFrames();
    }

    private void initFrames() {
        logger.info("Initializing Frames");
        for (int i = 0; i < 10; i++) {
            this.frames.add(new Frame(i));
        }
        this.currentFrame = this.frames.get(0);
        logger.info("Initialized " + this.frames.size() + " Frames");
    }

    public void roll(int pins) {
        if (pins < MIN_PINS) {
            throw new IllegalStateException("Negative roll is invalid");
        }
        if (pins > MAX_PINS) {
            throw new IllegalStateException("Pin count exceeds pins on the lane");
        }

        if (!currentFrame.isFrameFull()) {
            currentFrame.rolls.add(pins);
        } else {
            logger.info("Frame: " + (currentFrame.id + 1) + " is Full. Getting next one.");
            currentFrame = frames.get(currentFrame.id + 1);
            roll(pins);
        }

        if (!currentFrame.is10thFrame() && currentFrame.getSumOfRolls() > MAX_PINS) {
            throw new IllegalStateException("Pin count exceeds pins on the lane");
        }
        if (currentFrame.is10thFrame()) {
            int roll1 = currentFrame.rolls.get(0);
            int maybe2 = currentFrame.rolls.size() >= 2 ? currentFrame.rolls.get(1) : 0;
            int maybe3 = currentFrame.rolls.size() >= 3 ? currentFrame.rolls.get(2) : 0;

            if (currentFrame.rolls.size() == 2) {
                if (roll1 != MAX_PINS && roll1 + maybe2 > MAX_PINS) {
                    throw new IllegalStateException("Pin count exceeds pins on the lane");
                }
            }

            if (currentFrame.rolls.size() == 3) {
                if (roll1 == MAX_PINS && maybe2 != MAX_PINS && maybe2 + maybe3 > MAX_PINS) {
                    throw new IllegalStateException("Pin count exceeds pins on the lane");
                }
                if (!currentFrame.isFillBallNeeded()) {
                    throw new IllegalStateException("Cannot roll after game is over");
                }
            }

            if (currentFrame.rolls.size() > 3) {
                throw new IllegalStateException("Cannot roll after game is over");
            }
        }
    }

    private int getFrameScore(Frame frame) {
        int sumOfRolls = frame.getSumOfRolls();

        if (!frame.is10thFrame()) {
            if (sumOfRolls < MAX_PINS) {
                logger.info("Frame " + (frame.id + 1) + " has score of " + sumOfRolls + " (OPEN Frame)");
                return sumOfRolls;
            } else if (frame.isSpare()) {
                int spareScore = sumOfRolls + frames.get(frame.id + 1).rolls.get(0);
                logger.info("Frame " + (frame.id + 1) + " has score of " + spareScore + " (SPARE)");
                return spareScore;
            } else if (frame.isStrike()) {
                int strikeScoe = sumOfRolls + get2RollsFromNextFrames(frame);
                logger.info("Frame " + (frame.id + 1) + " has score of " + strikeScoe + " (STRIKE)");
                return strikeScoe;
            }
        } else {
            return sumOfRolls;
        }

        return -1;
    }

    private int get2RollsFromNextFrames(Frame frame) {
        if (frames.get(frame.id + 1).rolls.size() >= 2) {
            return frames.get(frame.id + 1).rolls.get(0) + frames.get(frame.id + 1).rolls.get(1);
        } else {
            return frames.get(frame.id + 1).rolls.get(0) + frames.get(frame.id + 2).rolls.get(0);
        }
    }

    public int score() {
        if (!currentFrame.is10thFrameCompleted()) {
            throw new IllegalStateException("Score cannot be taken until the end of the game");
        }

        return frames.stream().map(x -> getFrameScore(x)).reduce(0, (x, y) -> x + y);
    }
}