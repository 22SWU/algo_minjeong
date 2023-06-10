// 2908: 상수

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B2908_상수 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        
        StringBuffer a = new StringBuffer(st.nextToken());
        StringBuffer b = new StringBuffer(st.nextToken());

        int c = Integer.parseInt(a.reverse().toString());
        int d = Integer.parseInt(b.reverse().toString());

        System.out.println(Math.max(c, d));
        // System.out.println(c>d ? c:d);
    }
}
