class RotationalCipher {

    private final int shiftKey;

    RotationalCipher(int shiftKey) {
        this.shiftKey = shiftKey;
    }

    String rotate(String data) {
        if(0 == shiftKey || 26 == shiftKey) return data;

        StringBuilder result = new StringBuilder();
        for(Character c : data.toCharArray()) {
            if (Character.isLetter(c)) {
                if(Character.isLowerCase(c)) {
                    result.append((char) ('a' + ((c - 'a' + shiftKey) % 26)));
                } else {
                    result.append((char) ('A' + ((c - 'A' + shiftKey) % 26)));
                }
            } else {
                result.append(c);
            }
        }

        return result.toString();
    }

}
