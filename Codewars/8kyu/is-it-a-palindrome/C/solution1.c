// C - Clang 3.6 / C11

#include <string.h>
#include <ctype.h>

int isPalindrom(const char *s) {
    int len = strlen(s);
    for (int i = 0; i < len / 2; ++i) {
        if (tolower(s[i]) != tolower(s[len - i - 1])) {
            return 0;
        }
    }
    return 1;
}
