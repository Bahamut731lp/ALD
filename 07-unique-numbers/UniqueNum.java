package aplicake;

import java.util.ArrayList;
import java.util.Scanner;

public class UniqueNum {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<Integer> allArr = new ArrayList();
        ArrayList<Integer> repeatArr = new ArrayList();
        ArrayList<Integer> uniqueArr;
        String input;
        String[] nums;
        String row = "";
        String all = "all: ", repeat = ">1x: ", unique = "=1x: ";
        while (sc.hasNextLine()) {
            input = sc.nextLine();
            row += input + ",";
            nums = input.split(",");
            for (int m = 0; m < nums.length; m++) {
                if (!allArr.contains(Integer.parseInt(nums[m]))) {
                    allArr.add(Integer.parseInt(nums[m]));
                }

            }
        }
        nums = row.split(",");

        for (int m = 0; m < nums.length - 1; m++) {
            for (int n = m + 1; n < nums.length; n++) {
                if (nums[m].equals(nums[n]) && !repeatArr.contains(Integer.parseInt(nums[m]))) {
                    repeatArr.add(Integer.parseInt(nums[m]));
                }

            }
        }

        uniqueArr = findUnique(allArr, repeatArr);
        all = all + allArr.toString().substring(1, allArr.toString().length() - 1).replaceAll("\\s", "");
        repeat = repeat + repeatArr.toString().substring(1, repeatArr.toString().length() - 1).replaceAll("\\s", "");
        unique = unique + uniqueArr.toString().substring(1, uniqueArr.toString().length() - 1).replaceAll("\\s", "");
        System.out.println(all);
        System.out.println(repeat);
        System.out.println(unique);
    }
    public static ArrayList<Integer> findUnique(ArrayList<Integer> arr1, ArrayList<Integer> arr2) {
        ArrayList<Integer> uniqueArr = new ArrayList();
        boolean repeat;
        for (int i = 0; i < arr1.size(); i++) {
            repeat = true;
            for (int j = 0; j < arr2.size(); j++) {
                if (arr1.get(i).equals(arr2.get(j))) {
                    repeat = false;
                }
            }
            if (repeat) {
                uniqueArr.add(arr1.get(i));
            }

        }
        return uniqueArr;
    }
}
