public class Twofer {
    public String twofer(String inputName) {
        String exitName = new String();

        if(inputName == null) {
            exitName = "you";
        } else {
            exitName = inputName;
        }

        return "One for " + exitName + ", one for me.";
    }
}