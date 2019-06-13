package section_07.challenges.oop_master_challenge;

public enum BreadRoll {
    Wheat("Wheat"),
    BrownRye("Brown Rye"),
    Dark("Dark"),
    Deluxe("Deluxe");

    private final String name;

    BreadRoll(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }
}
