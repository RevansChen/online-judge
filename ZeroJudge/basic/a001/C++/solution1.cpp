// g++ -std=c++14(gcc 5.4.0)

#include <iostream>
#include <string>

using std::string;
using std::cin;
using std::cout;
using std::endl;

int main() {
    string s;
    
    while (cin >> s) {
        cout << "hello, " << s << endl;
    }
    
    return 0;
}
