package section_07.challenges.oop_master_challenge;

import java.util.ArrayList;
import java.util.List;

public class Hamburger {
    protected String name;
    private BreadRoll breadRoll;
    private double basePrice;
    private List<Additions> additions;
    private int maximumNoOfAddtitions;

    public Hamburger(String name, BreadRoll breadRoll, double basePrice, List<Additions> additions, int maximumNoOfAddtitions) {
        this.name = name;
        this.breadRoll = breadRoll;
        this.basePrice = basePrice;
        this.additions = additions;
        this.maximumNoOfAddtitions = maximumNoOfAddtitions;
    }

    public Hamburger(String name, BreadRoll breadRoll, double basePrice, int maximumNoOfAddtitions) {
        this(name, breadRoll, basePrice, new ArrayList<>(), maximumNoOfAddtitions);
    }

    public Hamburger(String name, BreadRoll breadRoll, double basePrice) {
        this(name, breadRoll, basePrice, new ArrayList<>(), 0);
    }

    public String getName() {
        return name;
    }

    public BreadRoll getBreadRoll() {
        return breadRoll;
    }

    public double getBasePrice() {
        return basePrice;
    }

    public List<Additions> getAdditions() {
        return additions;
    }

    public void addAddition(Additions additionalAddition) {
        if (additions.size() < maximumNoOfAddtitions) {
            additions.add(additionalAddition);
        }
    }

    public void addAdditions(List<Additions> additionalAdditions) {
        if (additions.size() + additionalAdditions.size() <= maximumNoOfAddtitions) {
            additions.addAll(additionalAdditions);
        }
    }

    public void removeAddition(Additions addition) {
        additions.remove(addition);
    }

    public double getTotalPrice() {
        double additionsTotal = 0.00d;
        for (Additions addition : additions) {
            additionsTotal += addition.getPrice();
        }
        return basePrice + additionsTotal;
    }

    public String getBill() {
        StringBuilder sb = new StringBuilder();
        for (Additions addition : additions) {
            sb.append("\n  - ");
            sb.append(addition.getName());
        }

        if (sb.length() == 0) sb.append("NONE");

        return "~~~ Bills Burgers ~~~\n" +
                "Burger: " + name + "\n" +
                "Bread: " + breadRoll.getName() + "\n" +
                "Additions: " + sb.toString() + "\n" +
                "Total price: " + String.format("%.2f", getTotalPrice()) + "$";
    }
}
