package section_07.challenges.oop_master_challenge;

public enum Additions {
    drink("Drink", 2.5),
    fries("Fries", 3),
    tomato("Tomato", 0.5),
    lettuce("Lettuce", 0.30),
    onion("Onion", 0.6),
    friedOnion("Fried Onion", 1.0),
    sesame("Sesame", 2.0),
    cashewNuts("Cashew Nuts", 4.0);

    private final String name;
    private final double price;

    Additions(String name, double price) {
        this.name = name;
        this.price = price;
    }

    public String getName() {
        return name;
    }

    public double getPrice() {
        return price;
    }


}
