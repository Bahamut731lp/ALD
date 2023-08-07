package aplicake;

import java.util.Iterator;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class FIFO {

    public static void main(String[] args) {
         Scanner sc = new Scanner(System.in);
       Queue<String> que = new LinkedList<>();
        String modif;
         while (sc.hasNextLine()) {
            que.add(sc.nextLine());
        }
        for (Iterator<String> iterator = que.iterator(); iterator.hasNext();) {
            String orig = " " + que.poll();
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
