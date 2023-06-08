// 2480: 주사위 세개
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.lang.Math;

public class B2480_주사위세개 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        if(a==b && b==c){
            System.out.println(10000+(a*1000));
        }else if(a!=b && b!=c && a!=c){
            System.out.println(Math.max(Math.max(a, b), c)*100);
        }else{
            if (a==b || a==c){
                System.out.println(1000+(a*100));
            }else{
                System.out.println(1000+(b*100));
            }
        }
    }
}
