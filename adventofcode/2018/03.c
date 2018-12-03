#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct {
    int id, x, y, w, h;
} claim;

#define min(a, b) (((a) < (b)) ? (a) : (b))
#define max(a, b) (((a) > (b)) ? (a) : (b))

int sol1(claim *claims, size_t count) {
    int area[1000][1000];
    int result;

    for (size_t i = 0; i < 1000 * 1000; i++)
        area[i / 1000][i % 1000] = 0;

    for (size_t i = 0; i < count; i++)
        for (int ix = claims[i].x; ix < claims[i].x + claims[i].w; ix++)
            for (int iy = claims[i].y; iy < claims[i].y + claims[i].h; iy++)
                area[ix][iy]++;

    for (int ix = 0; ix < 1000; ix++)
        for (int iy = 0; iy < 1000; iy++)
            if (area[ix][iy] > 1)
                result++;

    return result;
}

int sol2(claim *claims, size_t count) {
    claim ca, cb;
    for (size_t a = 0; a < count; a++) {
        int overlaps = 0;
        ca = claims[a];
        for (size_t b = 0; b < count; b++) {
            cb = claims[b];
            if (a == b)
                continue;

            overlaps = (max(ca.x, cb.x) < min(ca.x+ca.w, cb.x+cb.w));
            overlaps = (max(ca.y, cb.y) < min(ca.y+ca.h, cb.y+cb.h)) && overlaps;

            if (overlaps)
                break;
        }
        if (!overlaps)
            return claims[a].id;
    }
    return 0;
}

int main() {
    claim claims[2000];
    size_t count;
    while (1) {
        claim c;
        int result = scanf(
            "#%d @ %d,%d: %dx%d\n",
            &(c.id), &(c.x), &(c.y), &(c.w), &(c.h));

        if (result == EOF) break;
        claims[count] = c;
        count++;
    }
    printf("%d\n", sol1(claims, count));
    printf("%d\n", sol2(claims, count));
    return 0;
}
