import java.util.Random;
import java.util.stream.IntStream;

class DnDCharacter {

    private final int strength;
    private final int dexterity;
    private final int constitution;
    private final int intelligence;
    private final int wisdom;
    private final int charisma;
    private final int hitpoints;

    public DnDCharacter() {
        strength = ability();
        dexterity = ability();
        constitution = ability();
        intelligence = ability();
        wisdom = ability();
        charisma = ability();
        hitpoints = 10 + modifier(getConstitution());
    }

    int ability() {
        Random rand = new Random();
        return IntStream.range(0, 4).map(x -> rand.nextInt(1, 7)).sorted().skip(1).sum();
    }

    int modifier(int input) {
        return input > 10 ? -(10 - input) / 2 : -(11 - input) / 2;
    }

    int getStrength() {
        return strength;
    }

    int getDexterity() {
        return dexterity;
    }

    int getConstitution() {
        return constitution;
    }

    int getIntelligence() {
        return intelligence;
    }

    int getWisdom() {
        return wisdom;
    }

    int getCharisma() {
        return charisma;
    }

    int getHitpoints() {
        return hitpoints;
    }

}
