// 11654: 아스키 코드

import java.util.Scanner;

public class B11654_아스키코드 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        char ch =  sc.nextLine().charAt(0);
        int num = (int)ch;

        System.out.println(num);
    }
}
