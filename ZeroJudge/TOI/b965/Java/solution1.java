import java.util.Scanner;
import java.util.Stack;

public class JAVA {
    private static int row = 0;
    private static int col = 0;
    private static int[] arr = new int[100];

    private static void flip() {
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

    private static void rotate() {
        int[] tmp = new int[100];
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

    private static void printAnswer() {
        System.out.printf("%d %d%n", row, col);
        for (int r = 0; r < row; ++r) {
            System.out.printf("%d", arr[r * col]);
            for (int c = 1; c < col; ++c) {
                System.out.printf(" %d", arr[r * col + c]);
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        Scanner cin = new Scanner(System.in);
        Stack<Integer> ops = new Stack<Integer>();
		while (cin.hasNext()) {
			row = cin.nextInt();
			col = cin.nextInt();
            int num = cin.nextInt();
            
            for (int i = 0; i < row * col; ++i) {
                arr[i] = cin.nextInt();
            }
            for (int i = 0; i < num; ++i) {
                ops.push(cin.nextInt());
            }
            
            while (!ops.empty()) {
                Integer op = ops.pop();
                if (op == 1) {
                    flip();
                }
                else {
                    rotate();
                }
            }
            printAnswer();
        }
    }
}
