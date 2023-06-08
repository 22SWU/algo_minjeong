// 2438: 별찍기 - 1

import java.util.Scanner;

public class B2438_별찍기_1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = Integer.parseInt(sc.nextLine());

        String star = "*";
        for(int i=1; i<=num; i++){
            System.out.println(star);
            star += "*";
        }
    }
}
