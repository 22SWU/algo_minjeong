// 9086: 문자열

import java.util.Scanner;

public class B9086_문자열 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int num = Integer.parseInt(sc.nextLine());

        for(int i=0; i<num; i++){
            String[] str = sc.nextLine().split("");
            System.out.println(str[0]+str[str.length-1]);
        }
    }
}
