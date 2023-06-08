// 10810: 공 넣기
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B10810_공넣기 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] arr = new int[N];
        for(int l=0; l<M; l++){
            st = new StringTokenizer(br.readLine(), " ");
            int i = Integer.parseInt(st.nextToken());
            int j = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());

            for(int m=i-1; m<j; m++){
                arr[m] = k;
            }
        }
        for (int i:arr){
            System.out.print(i+" ");
        }
    }
}
