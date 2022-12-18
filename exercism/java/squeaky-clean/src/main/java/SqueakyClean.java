import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

class SqueakyClean {
    static String clean(String identifier) {
        String transform1 = identifier.replaceAll(" ", "_");
        String transform2 = transform1.replaceAll("\\p{Cc}", "CTRL");
        String transform3 = doTransform3(transform2);
        String transform4 = transform3.chars()
                .mapToObj(x -> (char) x)
                .filter(c -> Character.isAlphabetic(c) || c == '_')
                .map(c -> String.valueOf(c))
                .collect(Collectors.joining());
        String transform5 = transform4.replaceAll("[α-ω]", "");

        return transform5;
    }

    static String doTransform3(String input) {
        StringBuffer sb = new StringBuffer();
        for (int i = 0; i < input.length(); i++) {
            if (input.charAt(i) == '-' && i < input.length() - 1) {
                i += 1;
                sb.append(Character.toUpperCase(input.charAt(i)));
            } else {
                sb.append(input.charAt(i));
            }
        }
        return sb.toString();
    }
}
