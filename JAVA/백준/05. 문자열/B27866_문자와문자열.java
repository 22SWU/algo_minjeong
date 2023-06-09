// 27866: 문자와 문자열

import java.util.Scanner;

public class B27866_문자와문자열 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] str = sc.nextLine().split("");
        int num = Integer.parseInt(sc.nextLine());

        System.out.println(str[num-1]);
    }
}
