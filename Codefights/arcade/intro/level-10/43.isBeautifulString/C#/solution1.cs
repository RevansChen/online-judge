bool isBeautifulString(string inputString) {
    Dictionary<char, int> dict = new Dictionary<char, int>();
    foreach (char c in inputString) {
        if (!dict.ContainsKey(c)) {
            dict[c] = 0;
        }
        dict[c] += 1;
    }

    int count = 0;
    if (dict.ContainsKey('a')) {
        count = dict['a'];
    }
    for (char c = 'b'; c <= 'z'; ++c) {
        if (dict.ContainsKey(c)) {
            if (dict[c] > count) {
                return false;
            }
            count = dict[c];
        }
        else {
            count = 0;
        }
    }
    return true;
}
