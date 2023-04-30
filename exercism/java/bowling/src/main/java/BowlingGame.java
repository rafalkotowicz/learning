/*

Since this exercise has a difficulty of > 4 it doesn't come
with any starter implementation.
This is so that you get to practice creating classes and methods
which is an important part of programming in Java.

Please remove this comment when submitting your solution.

*/


import java.util.ArrayList;
import java.util.logging.Logger;

enum FrameState {
    Open,
    Spare,
    Strike,
    New
}


class Frame {
    public int id;
    public ArrayList<Integer> rolls;
    public FrameState state;

    public Frame(int id) {
        this.id = id;
        this.rolls = new ArrayList<>();
        this.state = FrameState.New;
    }
}

public class BowlingGame {
    private final ArrayList<Frame> frames;
    private Frame currentFrame;
    private final Logger logger = Logger.getLogger(BowlingGame.class.getName());

    public BowlingGame() {
        this.frames = new ArrayList<Frame>();
        initFrames();
    }

    private void initFrames() {
        this.logger.info("Initializing Frames");
        for (int i = 1; i <= 10; i++) {
            this.frames.add(new Frame(i));
        }
        this.currentFrame = this.frames.get(0);
        this.logger.info("Initialized " + this.frames.size() + " Frames");
    }

    public void roll(int pins) {
        currentFrame.rolls.add(pins);
        if (currentFrame.rolls.size() >= 2){

        }
    }

    public int score() {
        return 0;
    }
}