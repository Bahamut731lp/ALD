package aplicake;

import java.util.Scanner;

/**
 *
 * @author TOMKO
 */
public class Answer42 {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int n = input.nextInt();

        while (n != 42) {

            System.out.println(n);

            n = input.nextInt();

        }
    }

}
