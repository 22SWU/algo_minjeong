// 5622: 다이얼 

import java.util.HashMap;
import java.util.Scanner;

public class B5622_다이얼 {
    public static void main(String[] args) {
        HashMap<String, Integer> map = new HashMap<String, Integer>(){{//초기값 지정
            put("A",3);
            put("B",3);
            put("C",3);

            put("D",4);
            put("E",4);
            put("F",4);

            put("G",5);
            put("H",5);
            put("I",5);

            put("J", 6);
            put("K", 6);
            put("L", 6);

            put("M", 7);
            put("N", 7);
            put("O", 7);

            put("P", 8);
            put("Q", 8);
            put("R", 8);
            put("S", 8);

            put("T", 9);
            put("U", 9);
            put("V", 9);

            put("W", 10);
            put("X", 10);
            put("Y", 10);
            put("Z", 10);
        }};

        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();

        int total = 0;
        for(int i=0; i<str.length(); i++){
            total += map.get(Character.toString(str.charAt(i))); // 수정: 문자를 문자열로 변환하여 맵의 키로 사용
        }
        System.out.println(total);
    }
}
