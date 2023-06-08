    // 1546: 평균

    import java.util.Scanner;
    import java.util.StringTokenizer;
    
    public class B1546_평균 {
        public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);
            int num = Integer.parseInt(sc.nextLine());
            StringTokenizer st = new StringTokenizer(sc.nextLine(), " ");

            Double[] arr = new Double[num];
            double max = 0;
            for(int i=0; i<num;i++){
                arr[i]=Double.parseDouble(st.nextToken());
                if(max<arr[i]){
                    max = arr[i];
                }
            }

            double total = 0;
            for(Double i:arr){
                total += i/max*100;
            }
            System.out.println(total/num);
        }
    }
