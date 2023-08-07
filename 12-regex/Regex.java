package aplicake;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 *
 * @author TOMKO
 */
public class Regex {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        //Pattern preprijmeni = Pattern.compile(".*Jmeno:.*$");
        //Pattern titul = Pattern.compile(".*Tituly: \">.*$");
        Pattern prijmeni = Pattern.compile(".*<span class=\"xg_hide\">(?:<.*>)*([^<]*)<.*$");
        Pattern jmeno = Pattern.compile("(.*)");
        Pattern id = Pattern.compile("(.*)&nbsp;<a");
        Pattern obor = Pattern.compile(".*Stav: \">(.*)<.*$");
        ArrayList<ArrayList<String>> students = new ArrayList<>();
        ArrayList<String> names = new ArrayList<>();
        String line = "";
        while (!line.equals("0")) {
            line = sc.nextLine();
            if (line.contains("Jmeno:")) {
                line = sc.nextLine();
                names.add(getData(prijmeni, line));
            }

            if (line.contains("Tituly:")) {
                line = sc.nextLine();
                names.add(getData(jmeno, line));
            }

            if (line.contains("Fakulta:")) {
                line = sc.nextLine();
                String fullID = getData(id, line);
                names.add(fullID.substring(0, 1));
                names.add(fullID.substring(1));
            }
            if (line.contains("Stav:")) {
                names.add(getData(obor, line));
            }

            if (names.size() == 5) {
                students.add(new ArrayList<>(names));
                names.removeAll(names);
            }

        }
        sortListList(students);
        getGroup(students, "AI");
        getGroup(students, "AVI");
        getGroup(students, "IS");
        getGroup(students, "IT");
    }

    public static void sortListList(ArrayList<ArrayList<String>> data) {
        for (ArrayList<String> num : data) {
            if (Integer.parseInt(num.get(3)) % 2 != 0) {
                num.set(3, "-" + num.get(3));
            }
        }
        Collections.sort(data, (ArrayList<String> a1, ArrayList<String> a2) -> {
            try {
                return a1.get(3).compareTo(a2.get(3));
            } catch (NullPointerException e) {
                return 0;

            }
        });
        for (ArrayList<String> num : data) {
            if (Integer.parseInt(num.get(3)) % 2 != 0) {
                num.set(3, num.get(3).substring(1));
            }
        }
    }

    public static String getData(Pattern p, String line) {
        Matcher m = p.matcher(line);
        if (m.find()) {
            return m.group(1).trim();
        }
        return "0";
    }

    public static void getGroup(ArrayList<ArrayList<String>> students, String group) {
        System.out.println(group + ":");
        String pismeno, prijmeni, jmeno, name, obor, id;
        int count = 1;
        for (int m = 0; m < students.size(); m++) {
            if (students.get(m).contains(group)) {
                pismeno = students.get(m).get(2);
                prijmeni = students.get(m).get(0).toUpperCase();
                jmeno = students.get(m).get(1);
                name = prijmeni + " " + jmeno;
                obor = students.get(m).get(4);
                id = students.get(m).get(3);
                System.out.format("%2d: %s %-18s %-3s %s\n", count, pismeno, name, obor, id);
                count += 1;
            }

        }
        System.out.println();
    }

}
