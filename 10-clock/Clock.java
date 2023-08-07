package aplicake;

import java.util.Scanner;

/**
 *
 * @author TOMKO
 */
public class Clock {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String clock = "";
        String[] time;
        int[] segs = new int[7];
        int temp;
        int hod, min, sek;
        int num = 0;
        while (true) {
            temp = 0;
            nullArr(segs);
            for (int i = 0; i < 3; i++) {
                clock = sc.nextLine();

                time = clock.split(":");

                if (!time[1].equals(" broken")) {
                    num = Integer.parseInt(time[0].substring(6));
                    hod = Integer.parseInt(time[1].trim());
                    min = Integer.parseInt(time[2]);
                    sek = Integer.parseInt(time[3]);
                } else {
                    hod = -1;
                    min = -1;
                    sek = -1;
                }
                if (checkHour(segs, num, hod, min, sek) == 1) {
                    temp = 1;
                }
            }

            System.out.print(getNum(segs));
            if (sc.nextLine().equals("---")) {
                break;
            }
        }

    }

    static void nullArr(int[] segs) {
        for (int i = 0; i < 7; i++) {
            segs[i] = 0;
        }
    }

    static int checkHour(int[] Arr, int num, int hod, int min, int sec) {
        int tmp = 0;
        if (hod < 0) {
            tmp = 1;
        }
        if (tmp == 1 || (hod % 3 == 0 && min % 15 == 0 && sec % 15 == 0)) {

            switch (num) {

                case 1:
                    if (tmp == 1) {
                        return 1;
                    }

                    if (hod % 12 == 9 || min % 60 == 45 || sec % 60 == 45) {
                        Arr[0] = 1;
                    }

                    if (hod % 12 == 6 || min % 60 == 30 || sec % 60 == 30) {
                        Arr[1] = 1;
                    }
                    break;

                case 2:
                    if (tmp == 1) {
                        return 1;
                    }

                    if (hod % 12 == 0 || min % 60 == 0 || sec % 60 == 0) {
                        Arr[2] = 1;
                    }

                    if (hod % 12 == 9 || min % 60 == 45 || sec % 60 == 45) {
                        Arr[3] = 1;
                    }
                    break;

                case 3:
                    if (tmp == 1) {
                        break;
                    }

                    if (hod % 12 == 6 || min % 60 == 30 || sec % 60 == 30) {
                        Arr[4] = 1;
                    }

                    if (hod % 12 == 0 || min % 60 == 0 || sec % 60 == 0) {
                        Arr[5] = 1;
                    }

                    if (hod % 12 == 3 || min % 60 == 15 || sec % 60 == 15) {
                        Arr[6] = 1;
                    }
                    break;

                default:
                    break;
            }
        } else {
            return 1;
        }
        return 0;
    }

    static int getSum(int[] Arr) {
        int sum = 0;
        for (int m = 0; m < 7; m++) {
            sum += Arr[m];
        }
        return sum;
    }

    static char getNum(int[] Arr) {

        switch (getSum(Arr)) {

            case 2:
                if (Arr[1] == 1 && Arr[2] == 1) {
                    return '1';
                }
                break;

            case 3:
                if (Arr[0] == 1 && Arr[1] == 1 && Arr[2] == 1) {
                    return '7';
                }
                break;

            case 4:
                if (Arr[0] == 0 && Arr[3] == 0 && Arr[4] == 0) {
                    return '4';
                }

                break;

            case 5:
                if (Arr[2] == 0 && Arr[5] == 0) {
                    return '2';
                }
                if (Arr[4] == 0 && Arr[5] == 0) {
                    return '3';
                }
                if (Arr[1] == 0 && Arr[4] == 0) {
                    return '5';
                }
                break;

            case 6:

                if (Arr[6] == 0) {
                    return '0';
                }

                if (Arr[1] == 0) {
                    return '6';
                }

                if (Arr[4] == 0) {
                    return '9';
                }
                break;

            case 7:
                return '8';

        }
        return 0;
    }
}
