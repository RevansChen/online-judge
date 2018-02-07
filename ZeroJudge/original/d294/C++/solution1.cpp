// g++ -std=c++14(gcc 5.4.0)

#include <iostream>
using namespace std;

int main() {
    uint64_t n, m;
    
    while (cin >> n >> m) {
        cout << ((n * (n + 1)) / 2) * ((m * (m + 1)) / 2) << endl;
    }

    return 0;
}
