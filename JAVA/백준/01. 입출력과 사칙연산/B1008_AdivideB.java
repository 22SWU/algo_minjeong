// 1008: A/B

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B1008_AdivideB {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        double a = Integer.parseInt(st.nextToken());
        double b = Integer.parseInt(st.nextToken());
        
        System.out.println(a/b);
    }
}
