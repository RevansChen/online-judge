// gcc -std=c11(gcc 5.4.0)

#include <stdio.h>

void swap(int *a, int *b) {
    int x = *a;
    *a = *b;
    *b = x;
}

void flip(int row, int col, int *arr) {
    for (int r = 0; r < row / 2; ++r) {
        for (int c = 0; c < col; ++c) {
            int idx1 = r * col + c;
            int idx2 = (row - r - 1) * col + c;
            swap(&arr[idx1], &arr[idx2]);
        }
    }
}

void rotate(int *row, int *col, int *arr) {
    int tmp[100] = {0};
    int i = 0;
    for (int c = (*col) - 1; c >= 0; --c) {
        for (int r = 0; r < (*row); ++r) {
            tmp[i++] = arr[r * (*col) + c];
        }
    }
    swap(row, col);
    for (int i = 0; i < (*row) * (*col); ++i) {
        arr[i] = tmp[i];
    }
}

void printAnswer(int row, int col, int *arr) {
    printf("%d %d\n", row, col);
    for (int r = 0; r < row; ++r) {
        printf("%d", arr[r * col]);
        for (int c = 1; c < col; ++c) {
            printf(" %d", arr[r * col + c]);
        }
        putchar('\n');
    }
}

int main() {
    int row = 0, col = 0, num = 0;
    int arr[100] = {0};
    int ops[10] = {0};

    while (scanf("%d %d %d", &row, &col, &num) != EOF) {
        for (int i = 0; i < row * col; ++i) {
            scanf("%d", &arr[i]);
        }
        for (int i = 0; i < num; ++i) {
            scanf("%d", &ops[i]);
        }
        while (num--) {
            int op = ops[num];
            if (op) {
                flip(row, col, arr);
            }
            else {
                rotate(&row, &col, arr);
            }
        }
        printAnswer(row, col, arr);
    }
    
    return 0;
}
