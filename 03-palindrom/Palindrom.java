package aplicake;

/**
 *
 * @author TOMKO
 */
import java.util.Scanner;

public class Palindrom {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String slovo;
        while(sc.hasNextLine()) {
            slovo = sc.next().toLowerCase();
            sc.nextLine();
            int delka = slovo.length();
            boolean isPal = true;
            for (int i = 0; i <= delka / 2; i++) {
                if (slovo.charAt(i) != slovo.charAt(delka - 1 - i)) {
                    isPal = false;
                    break;
                }
            }
            System.out.println(isPal ? "ano" : "ne");
        }
    }

}
