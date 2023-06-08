// 5597: 과제 안 내신 분..?

import java.util.Scanner;

public class B5597_과제안내신분 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        boolean[] student = new boolean[30];

        for(int i=0; i<28; i++){
            int cur = Integer.parseInt(sc.nextLine());
            student[cur-1] = true;
        }

        for(int i=0; i<student.length; i++){
            if(!student[i]){
                System.out.println(i+1);
            } 
        }
    }
}
