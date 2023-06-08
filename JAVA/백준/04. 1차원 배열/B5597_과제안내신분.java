// 5597: 과제 안 내신 분..?

import java.util.Scanner;

public class B5597_과제안내신분 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] student = new int[30];

        for(int i=0; i<28; i++){
            int cur = Integer.parseInt(sc.nextLine());
            student[cur-1] = 1;
        }

        for(int i=0; i<student.length; i++){
            if(student[i]==0){
                System.out.println(i+1);
            } 
        }
    }
}
