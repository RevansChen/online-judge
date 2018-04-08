// gcc -std=c11(gcc 5.4.0)

#include <stdio.h>

inline char read() {
    char ch = 0;
    do {
        ch = (char)getchar();
    } while (!isdigit(ch));
    return ch;
}

int main() {
    int row = 0, col = 0, num = 0;
    char arr[100] = {0};
    char tmp[100] = {0};
    char ops[10] = {0};

    while (scanf("%d %d %d", &row, &col, &num) != EOF) {
        for (int i = 0; i < (row * col); ++i) {
            arr[i] = read();
        }
        for (int i = 0; i < num; ++i) {
            ops[i] = read();
        }
        
        while (num--) {
            if (ops[num] == '1') {
                // flip
                for (int r = 0; r < (row >> 1); ++r) {
                    for (int c = 0; c < col; ++c) {
                        int idx1 = r * col + c;
                        int idx2 = (row - r - 1) * col + c;

                        // swap
                        char t = arr[idx1];
                        arr[idx1] = arr[idx2];
                        arr[idx2] = t;
                    }
                }
            }
            else {
                // rotate
                for (int c = col - 1, i = 0; c >= 0; --c) {
                    for (int r = 0; r < row; ++r) {
                        tmp[i++] = arr[r * col + c];
                    }
                }

                // swap
                int t = row;
                row = col;
                col = t;
                
                for (int i = 0; i < row * col; ++i) {
                    arr[i] = tmp[i];
                }
            }
        }

        // printAnswer
        printf("%d %d\n", row, col);
        for (int r = 0; r < row; ++r) {
            putchar(arr[r * col]);
            for (int c = 1; c < col; ++c) {
                putchar(' ');
                putchar(arr[r * col + c]);
            }
            putchar('\n');
        }
    }
    
    return 0;
}
