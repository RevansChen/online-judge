// g++ -std=c++14(gcc 5.4.0)

#include <iostream>
#define _USE_MATH_DEFINES
#include <cmath>

using std::fixed;
using std::cin;
using std::cout;
using std::endl;

int main() {
    double D, L;
    
    cout.precision(3);
    while (cin >> D >> L) {
        D /= 2;
        L /= 2;
        double halfA = L;
        double halfB = sqrt(L * L - D * D);
        cout << fixed << (M_PI * halfA * halfB) << endl;
    }

    return 0;
}
