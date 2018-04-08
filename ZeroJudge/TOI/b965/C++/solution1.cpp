// g++ -std=c++14(gcc 5.4.0)

#include <iostream>
#include <stack>
using namespace std;

void flip(int row, int col, int *arr) {
    int tmp[100] = {0};
    for (int r = 0; r < row / 2; ++r) {
        for (int c = 0; c < col; ++c) {
            int idx1 = r * col + c;
            int idx2 = (row - r - 1) * col + c;
            swap(arr[idx1], arr[idx2]);
        }
    }
}

void rotate(int &row, int &col, int *arr) {
    int tmp[100] = {0};
    int i = 0;
    for (int c = col - 1; c >= 0; --c) {
        for (int r = 0; r < row; ++r) {
            tmp[i++] = arr[r * col + c];
        }
    }
    swap(row, col);
    for (int i = 0; i < row * col; ++i) {
        arr[i] = tmp[i];
    }
}

void printAnswer(int row, int col, int *arr) {
    cout << row << ' ' << col << endl;
    for (int r = 0; r < row; ++r) {
        cout << arr[r * col];
        for (int c = 1; c < col; ++c) {
            cout << ' ' << arr[r * col + c];
        }
        cout << endl;
    }
}

int main() {
    int row = 0, col = 0, num = 0;
    int arr[100] = {0};
    stack<int> ops;

    while (cin >> row >> col >> num) {
        for (int i = 0; i < row * col; ++i) {
            cin >> arr[i];
        }
        for (int i = 0; i < num; ++i) {
            int tmp;
            cin >> tmp;
            ops.push(tmp);
        }
        while (!ops.empty()) {
            int op = ops.top();
            ops.pop();
            if (op) {
                flip(row, col, arr);
            }
            else {
                rotate(row, col, arr);
            }
        }
        printAnswer(row, col, arr);
    }
    
    return 0;
}
