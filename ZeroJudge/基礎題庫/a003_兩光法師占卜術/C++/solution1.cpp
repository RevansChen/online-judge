// g++ -std=c++14(gcc 5.4.0)

#include <iostream>
#include <string>
using namespace std;

int main() {
    int M, D;
    string table[3] = { "´¶³q", "¦N", "¤j¦N" };
    
    while (cin >> M >> D) {
        int S = (M * 2 + D) % 3;
        cout << table[S] << endl;
    }
    
    return 0;
}
