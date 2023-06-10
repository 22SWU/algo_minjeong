// 2675: 문자열 반복

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B2675_문자열반복 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int num = Integer.parseInt(br.readLine());
        for (int i=0; i<num; i++){
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken()); 
            String str = st.nextToken();

            for(int j=0; j<str.length(); j++){
                for(int l=0; l<n; l++){
                    System.out.print(str.charAt(j));
                }
            }
            System.out.println();
        }
    }
}
