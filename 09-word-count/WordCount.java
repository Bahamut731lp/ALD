package aplicake;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Locale;
import java.util.Map;
import java.util.Scanner;

/**
 *
 * @author TOMKO
 */
public class WordCount {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        HashMap<String, Integer> words = new LinkedHashMap<>();
        HashMap<String, Integer> pairs = new LinkedHashMap<>();
        double sum = 0;
        String text="";
        String textPair = "";

        while (!text.equals("0")) {
            text = sc.next().toLowerCase();
            if (words.containsKey(text)) {
                words.computeIfPresent(text, (k, v) -> v + 1);
            } else {
                words.put(text, 1);
            }
            if (sc.hasNextLine()) {
                textPair += text;
                if (!text.equals(textPair)) {
                    String[] pairArr = textPair.split(" ", 2);
                    if (pairArr[1].contains(" ")) {
                        textPair = pairArr[1];
                    }

                    if (pairs.containsKey(textPair)) {
                        pairs.computeIfPresent(textPair, (k, v) -> v + 1);
                    } else {
                        pairs.put(textPair, 1);
                    }
                }
                textPair += " ";
            }

        }
        for (double val : words.values()) {
            sum += val;
        }

        Map<String, Integer> wFreq = sortMap(words);
        Map<String, Integer> pFreq = sortMap(pairs);

        System.out.println("Word Frequency:");
        printFreqMap(wFreq, sum, 12);
        System.out.println("Phrase Frequency:");
        printFreqMap(pFreq, sum, 20);

    }

    public static Map<String, Integer> sortMap(Map<String, Integer> map) {
        List<Map.Entry<String, Integer>> list = new ArrayList<>(map.entrySet());
        list.sort(Map.Entry.comparingByValue(Comparator.reverseOrder()));

        Map<String, Integer> sorted = new LinkedHashMap<>();
        list.forEach(entry -> {
            sorted.put(entry.getKey(), entry.getValue());
        });
        return sorted;
    }

    public static void printFreqMap(Map<String, Integer> freq, double sum, int indent) {
        for (int k = 0; k < 15; k++) {
            Object[] keys = freq.keySet().toArray();
            int val = freq.get(keys[k].toString());
            double per = 100 * val / sum;

            System.out.format(Locale.ENGLISH, " - %-" + indent + "s %.2f%% (%d)%n", keys[k], per, val);

        }
    }

}
