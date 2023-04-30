class MicroBlog {
    public String truncateOld(String input) {

        StringBuilder truncated = new StringBuilder();

        final int length = input.length();
        int charsFound = 0;
        for (int offset = 0; offset < length; ) {
            final int codepoint = input.codePointAt(offset);
            truncated.append(Character.toChars(codepoint));
            charsFound++;
            if (charsFound == 5) {
                break;
            }
            offset += Character.charCount(codepoint);
        }
        return truncated.toString();
    }

    public String truncate(String input) {
        return input.codePoints().limit(5).collect(StringBuilder::new, (x, y) -> x.append(Character.toChars(y)),
                (a, b) -> a.append(",").append(b)).toString();
    }

}
