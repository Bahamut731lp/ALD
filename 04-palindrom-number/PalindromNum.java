package aplicake;

import java.util.Scanner;

/**
 *
 * @author TOMKO
 */
public class PalindromNum {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int delka, delkaNext, mid;
        String num = sc.next();
        String numNext, firstHalf;
        while (!num.equals("-1")) {
            String secondHalf = "";
            boolean evenDigits = (num.length() % 2) == 0;
            mid = evenDigits ? 0 : 1;
            delka = (num.length() / 2) + mid;
            firstHalf = num.substring(0, delka);
            for (int i = delka - 1 - mid; i >= 0; i--) {
                secondHalf += firstHalf.charAt(i);
            }
            numNext = firstHalf + secondHalf;

            if (num.length() <= 19 && (Long.parseLong(num) >= Long.parseLong(numNext))) {
                firstHalf = Long.toString(Long.parseLong(firstHalf) + 1);
                delkaNext = firstHalf.length();
                secondHalf = "";
                for (int i = delkaNext - 1 - mid; i >= 0; i--) {
                    secondHalf += firstHalf.charAt(i);
                }
                if (delkaNext > delka) {
                    firstHalf = firstHalf.substring(0, delka);
                }
                numNext = firstHalf + secondHalf;

            }
            System.out.println(numNext);
            num = sc.next();

        }
    }

}
