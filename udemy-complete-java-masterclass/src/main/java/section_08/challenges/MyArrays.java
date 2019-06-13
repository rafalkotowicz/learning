package section_08.challenges;

import java.util.Arrays;

public class MyArrays {
    public static int[] reverseSort(int[] in) {
        int[] out = Arrays.copyOf(in, in.length);

        while (isNotSortedDescending(out)) {
            for (int i = 1; i <= out.length - 1; i++) {
                if (out[i] > out[i - 1]) {
                    int swap = out[i];
                    out[i] = out[i - 1];
                    out[i - 1] = swap;
                }
            }
        }

        return out;
    }

    private static boolean isNotSortedDescending(int[] arr) {
        if (arr.length == 1) return true;
        for (int i = 1; i <= arr.length - 1; i++) {
            if (arr[i] > arr[i - 1]) return true;
        }

        return false;
    }
}
