package aplicake;

import java.util.Iterator;
import java.util.Scanner;
import java.util.Stack;

/**
 *
 * @author TOMKO
 */
public class LIFO {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Stack<String> stk = new Stack<>();
        String modif = "";
        while (sc.hasNextLine()) {
            stk.push(sc.nextLine());
            sc.nextLine();
        }
        for (Iterator<String> iterator = stk.iterator(); iterator.hasNext();) {
            String orig = " " + stk.pop();
            modif = "";
            for (int i = 0; i < orig.length();) {
                char znak = orig.charAt(i);
                if (znak == ' ') {
                    modif = modif + ' ' + Character.toUpperCase(orig.charAt(i + 1));
                    i = i + 2;
                } else {
                    modif = modif + znak;
                    i++;
                }
            }
            System.out.println(modif.trim());
        }
    }
}
