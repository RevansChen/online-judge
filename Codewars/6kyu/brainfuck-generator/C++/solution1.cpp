// C++ - 14

inline std::string to_brainfuck(const std::string& s_in) {
    std::string bf = "";
    for (int i = 0, val = 0; i < s_in.length(); ++i) {
        int diff = (int)s_in[i] - val;
        char ch = ((diff > 0) ? '+' : '-');
        for (int times = 0; times < abs(diff); ++times) {
            bf.push_back(ch);
        }
        bf.push_back('.');
        val += diff;
    }
    return bf;
}
