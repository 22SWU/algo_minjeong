// 8393: 합

import java.util.Scanner;

public class B8393_합 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int num = Integer.parseInt(sc.nextLine());
        int total = 0;
        for (int i=1; i<=num; i++){
            total += i;
        }
        System.out.println(total);
    }
}
