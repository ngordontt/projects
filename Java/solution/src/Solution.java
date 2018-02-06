
import java.util.*;

import static java.lang.System.out;


public class Solution {

    String word;

    public String getword(){
        return word;
    }
    private static int i;

    public static void loop(String i) {
        char[] strArray = i.toCharArray();
        int wordLength = i.length();
        int x;

        for (x = 0; x <= wordLength - 1; x++) {
            if (x % 2 == 0) {
                System.out.print(strArray[x]);
            }
            System.out.print(" ");

        for (x = 0; x <= wordLength - 1; x++) {
            if (x % 2 != 0) {
                System.out.print(strArray[x]);
            }
        }
        }
    }
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String word = in.next();

        loop(word);
    }
}
