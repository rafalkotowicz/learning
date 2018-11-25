package section_05.challenges;

public class FindNumbers {
    public static int sumOfNumbersDivisibleBy3And5(int start, int end, int breakCount) {
        int sum = 0;
        int count = 0;
        for(int i = start; i<=end; i++) {
            if(i % 3 == 0 && i % 5 == 0) {
                sum += i;
                count++;
            }
            if(count == breakCount) {
                break;
            }
        }
        return sum;
    }
}
