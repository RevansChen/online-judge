// C - Clang 3.6 / C11

#include <criterion/criterion.h>

int isPalindrom(const char *s);

Test(isPalindrom, should_pass_all_the_tests_provided) {
    cr_assert_eq(isPalindrom("a"), 1);
    cr_assert_eq(isPalindrom("aba"), 1);
    cr_assert_eq(isPalindrom("Abba"), 1);
    cr_assert_eq(isPalindrom("hello"), 0);
}
