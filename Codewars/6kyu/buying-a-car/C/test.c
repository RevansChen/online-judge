// C - Clang 3.6 / C11

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <criterion/criterion.h>

int* nbMonths(int startPriceOld, int startPriceNew, int savingperMonth, double percentLossByMonth);
char* array2StringInt(int * array, size_t sz);

void dotest(int startPriceOld, int startPriceNew, int savingperMonth, double percentLossByMonth, int *expr) {
    char* sexpr = array2StringInt(expr, 2);
    int *act = nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth);
    char* sact = array2StringInt(act, 2);
    if (strcmp(sact, sexpr) != 0) {
        printf("Error. Expected %s but got %s\n", sexpr, sact);
    }
    cr_assert_str_eq(sact, sexpr, "");

    free(sact);
    sact = NULL;
    free(sexpr);
    sexpr = NULL;
    free(act);
    act = NULL;
}

Test(nbMonths, ShouldPassAllTheTestsProvided) {
    {
        int r1[2] = { 6, 766 };
        dotest(2000, 8000, 1000, 1.5, r1);
    }
    {
        int r1[2] = { 0, 4000 };
        dotest(12000, 8000, 1000, 1.5, r1);
    }
    {
        int r1[2] = { 8, 597 };
        dotest(8000, 12000, 500, 1, r1);
    }
}

