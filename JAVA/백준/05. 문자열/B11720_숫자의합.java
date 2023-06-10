// 11720: 숫자의 합

import java.util.Scanner;

public class B11720_숫자의합 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = Integer.parseInt(sc.nextLine());
        String str = sc.nextLine();
        int total = 0;
        for(int i=0; i<num; i++){
            total += (int)str.charAt(i)-48;
        }
        System.out.println(total);
    }
}
