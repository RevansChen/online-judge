#include <stdio.h>

#define BUFFER_SIZE 16

int main() {
    char inp[BUFFER_SIZE];
    while (fgets(inp, BUFFER_SIZE, stdin) != NULL) {
        if (inp[0] == '#') {
            // 十六進位 轉 十進位
            int color;
            sscanf(inp, "#%X", &color);

            int r = (color >> 16) & 0xff;
            int g = (color >> 8) & 0xff;
            int b = color & 0xff;
            printf("%d %d %d\n", r, g, b);
        }
        else {
            // 十進位 轉 十六進位
            int r, g, b;
            sscanf(inp, "%d %d %d", &r, &g, &b);

            int color = r << 16 | g << 8 | b;
            printf("#%06X\n", color);
        }
    }
    return 0;
}
