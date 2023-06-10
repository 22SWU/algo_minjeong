// 10809: 알파벳 찾기

import java.util.Arrays;
import java.util.Scanner;

public class B10809_알파벳찾기 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        int[] arr = new int[26];

        for (int i=0; i<26; i++){
            arr[i] = -1;
        }

        for(int i=0; i<str.length(); i++){
            char chr = str.charAt(i);
            if (arr[chr-97] == -1){
                arr[chr-97] = i;
            }
        }

        for(int i:arr){
            System.out.print(i+" ");
        }
    }
}
