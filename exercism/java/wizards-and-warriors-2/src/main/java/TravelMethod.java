public enum TravelMethod {
    WALKING("by"),
    HORSEBACK("on");

    private final String preposition;

    TravelMethod(String preposition) {
        this.preposition = preposition;
    }

    public String getPreposition() {
        return preposition;
    }
}
