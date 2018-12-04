#include <stdio.h>
#include <math.h>
#include <stdint.h>
#include <stdlib.h>

int sol1(int *nums, size_t len) {
    int result;
    for (size_t i = 0; i < len; i++)
        result += nums[i];
    return result;
}

int sol2(int *nums, size_t len) {
    int result;
    int seen_pos[1000000], seen_neg[1000000];
    for (size_t i = 0; i < 1000000; i++) {
        seen_pos[i] = 0;
        seen_neg[i] = 0;
    }
    seen_pos[0] = 1;
    while (1) {
        for (size_t i = 0; i < len; i++) {
            result += nums[i];
            int *seen = (result >= 0) ? seen_pos : seen_neg;
            seen[abs(result)]++;
            if (seen[abs(result)] > 1)
                return result;
        }
    }
    return 0;
}

int main() {
    int nums[10000], n;
    size_t len = 0;
    while (scanf("%d\n", &n) != EOF) {
        nums[len] = n;
        len++;
    }
    printf("%d\n", sol1(nums, len));
    printf("%d\n", sol2(nums, len));
    return 0;
}
