import java.util.Scanner;
import java.util.Stack;

public class JAVA {
    public static void main(String[] args) {
        int row = 0, col = 0, num = 0;
        int[] arr = new int[100];
        int[] tmp = new int[100];
        int[] ops = new int[10];

        Scanner cin = new Scanner(System.in);
		while (cin.hasNext()) {
			row = cin.nextInt();
			col = cin.nextInt();
            num = cin.nextInt();
            
            for (int i = 0; i < row * col; ++i) {
                arr[i] = cin.nextInt();
            }
            for (int i = 0; i < num; ++i) {
                ops[i] = cin.nextInt();
            }

            while (num > 0) {
                int op = ops[--num];
                if (op == 1) {
                    for (int r = 0; r < row / 2; ++r) {
                        for (int c = 0; c < col; ++c) {
                            int idx1 = r * col + c;
                            int idx2 = (row - r - 1) * col + c;
            
                            int t = arr[idx1];
                            arr[idx1] = arr[idx2];
                            arr[idx2] = t;
                        }
                    }
                }
                else {
                    for (int c = col - 1, i = 0; c >= 0; --c) {
                        for (int r = 0; r < row; ++r) {
                            tmp[i++] = arr[r * col + c];
                        }
                    }
                    int t = row;
                    row = col;
                    col = t;
                    for (int i = 0; i < row * col; ++i) {
                        arr[i] = tmp[i];
                    }
                }
            }

            System.out.println(row + " " + col);
            for (int r = 0; r < row; ++r) {
                System.out.print(arr[r * col]);
                for (int c = 1; c < col; ++c) {
                    System.out.print(" " + arr[r * col + c]);
                }
                System.out.println();
            }
        }
    }
}
