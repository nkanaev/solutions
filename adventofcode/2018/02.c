#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int sol1(char **strings, size_t count) {
    char lettercount[26];
    int count2 = 0, count3 = 0;
    for (size_t i = 0; i < count; i++) {
        char *line = strings[i];
        for (size_t x = 0; x < 26; x++)
            lettercount[x] = 0;
        for (size_t x = 0; x < strlen(line); x++) {
            lettercount[line[x] - 'a']++;
        }

        int has2 = 0;
        int has3 = 0;
        for (size_t x = 0; x < 26; x++) {
            if (lettercount[x] == 2) has2 = 1;
            if (lettercount[x] == 3) has3 = 1;
        }
        if (has2) count2++;
        if (has3) count3++;
    }
    return count2 * count3;
}

char *sol2(char **strings, size_t count) {
    for (size_t x = 0; x < count - 1; x++) {
        for (size_t y = x + 1; y < count; y++) {
            size_t diffIdx;
            int diff = 0;
            for (size_t n = 0; n < strlen(strings[x]) && diff < 2; n++)
                if (strings[x][n] != strings[y][n]) {
                    diff++;
                    diffIdx = n;
                }
            if (diff == 1) {
                char *result = malloc(sizeof(char) * 100);
                strncpy(result, strings[x], diffIdx);
                strncpy(&result[diffIdx], &strings[x][diffIdx + 1],
                        strlen(strings[x]) - diffIdx - 1);
                result[strlen(strings[x])] = '\n';
                return result;
            }
        }
    }
    return NULL;
}

int main() {
    char **strings = malloc(sizeof(char *) * 250);
    char *line = malloc(sizeof(char) * 100);
    size_t count = 0;
    while (scanf("%s\n", line) != EOF) {
        strings[count] = line;
        line = malloc(sizeof(char) * 100);
        count++;
    }
    printf("%d\n", sol1(strings, count));
    printf("%s\n", sol2(strings, count));
    return 0;
}
