// g++ -std=c++14(gcc 5.4.0)

#include <iostream>

using std::cin;
using std::cout;
using std::endl;

int main() {
    int a, b;
    
    while (cin >> a >> b) {
        cout << a + b << endl;
    }
    
    return 0;
}
