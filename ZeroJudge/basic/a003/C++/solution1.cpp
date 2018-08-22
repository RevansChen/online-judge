// g++ -std=c++14(gcc 5.4.0)

#include <iostream>
#include <string>

using std::string;
using std::cin;
using std::cout;
using std::endl;

int main() {
    int M, D;
    string table[3] = { "普通", "吉", "大吉" };
    
    while (cin >> M >> D) {
        int S = (M * 2 + D) % 3;
        cout << table[S] << endl;
    }
    
    return 0;
}
