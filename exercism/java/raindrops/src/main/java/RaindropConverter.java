class RaindropConverter {

    String convert(int number) {
        StringBuilder rainDropSays = new StringBuilder();
        if(number % 3 == 0) { rainDropSays.append("Pling"); }
        if(number % 5 == 0) { rainDropSays.append("Plang"); }
        if(number % 7 == 0) { rainDropSays.append("Plong"); }
        return rainDropSays.toString().length() == 0 ? Integer.toString(number) : rainDropSays.toString();
    }

}
