// g++ -std=c++14(gcc 5.4.0)

#include <iostream>

using std::cin;
using std::cout;
using std::endl;

const size_t NUM = 10;
const int BENCH_HEIGHT = 30;

int main() {
    int h[NUM];

    while (cin >> h[0]) {
        for (int i = 1; i < NUM; ++i) {
            cin >> h[i];
        }
        
        int m;
        cin >> m;
        m += BENCH_HEIGHT;
        
        int count = 0;
        for (int i = 0; i < NUM; ++i) {
            if (m >= h[i]) {
                count++;
            }
        }
        cout << count << endl;
    }
    
    return 0;
}
