// g++ -std=c++14(gcc 5.4.0)

#include <iostream>

using std::cin;
using std::cout;
using std::endl;

int main() {
    uint64_t n, m;
    
    while (cin >> n >> m) {
        cout << ((n * (n + 1)) / 2) * ((m * (m + 1)) / 2) << endl;
    }

    return 0;
}
