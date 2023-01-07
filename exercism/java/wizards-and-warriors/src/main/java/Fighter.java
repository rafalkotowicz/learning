abstract class Fighter {
    private final String fighterType;
    protected boolean isVulnerable;

    public Fighter(String type) {
        fighterType = type;
        isVulnerable = false;
    }

    boolean isVulnerable() {
        return isVulnerable;
    }

    abstract int damagePoints(Fighter fighter);

    public String toString() {
        return String.format("Fighter is a %s", fighterType);
    }

}

class Warrior extends Fighter {

    public Warrior() {
        super("Warrior");
    }


    @Override
    int damagePoints(Fighter wizard) {
        return wizard.isVulnerable() ? 10 : 6;
    }
}

class Wizard extends Fighter {
    private boolean isSpellPrepared;

    public Wizard() {
        super("Wizard");
        isSpellPrepared = false;
    }

    @Override
    int damagePoints(Fighter warrior) {
        return isSpellPrepared ? 12 : 3;
    }

    void prepareSpell() {
        isSpellPrepared = true;
        isVulnerable = false;
    }

    @Override
    boolean isVulnerable() {
        return !isSpellPrepared;
    }

}
