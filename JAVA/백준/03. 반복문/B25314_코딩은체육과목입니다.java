//  25314: 코딩은 체육과목 입니다

import java.util.Scanner;

public class B25314_코딩은체육과목입니다 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = Integer.parseInt(sc.nextLine());

        num = num/4;

        for(int i=0; i<num; i++){
            System.out.print("long ");
        }
        System.out.print("int");
    }
}
