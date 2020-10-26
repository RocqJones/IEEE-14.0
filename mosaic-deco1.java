import java.util.Scanner;

public class Tiles {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n,cb_dollar, cp_dollar;
        n = in.nextInt();
        cb_dollar = in.nextInt();
        cp_dollar = in.nextInt();
        int sum_black= 0;
        int sum_pink = 0;

        int nLines[][] = new int[n][2];

        for(int x =0 ;x<n;x++){
            for(int y=0;y<2;y++){
                nLines[x][y] = in.nextInt();
            }
        }


        for(int x =0 ;x<n;x++){
            sum_black += nLines[x][0];
            sum_pink += nLines[x][1];
        }

        int black_p =(int)Math.ceil((double) sum_black / 10);
        int pink_p =(int)Math.ceil((double) sum_pink / 10);
        System.out.println((black_p * cb_dollar)+(pink_p * cp_dollar));
    }
}

/* 
SAMPLE INPUT
3 5 7
10 10
20 30
30 3

OUTPUT
65
*/