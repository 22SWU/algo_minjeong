// 2562: 최대값

import java.util.Scanner;

public class B2562_최대값 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int max = 0;
        int maxIndex = 0;
        for(int i=0; i<9; i++){
            int cur = Integer.parseInt(sc.nextLine());
            if(max<cur){
                max = cur;
                maxIndex = i;
            }
        }
        System.out.println(max);
        System.out.println(maxIndex+1);
    }
}
