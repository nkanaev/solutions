#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <math.h>
#include <string.h>

#define MIN(a, b) ((a) < (b) ? (a) : (b))

typedef struct node {
    char val;
    struct node *next, *prev;
} node;

node *to_list(const char *line, size_t len) {
    node *root, *cur;

    for (size_t i = 0; i < len; i++) {
        if (!isalpha(line[i])) continue;
        node *n = malloc(sizeof(node));
        n->val = line[i];
        n->next = n->prev = NULL;
        if (!root) {
            root = n;
            cur = n;
            continue;
        }
        n->prev = cur;
        cur->next = n;
        cur = n;
    }
    return root;
}

size_t sol1(const char *line, size_t len) {
    node *root = to_list(line, len);
    node *cur = root;
    while (cur) {
        if (cur->next && abs(cur->val - cur->next->val) == 32) {
            node *a = cur->prev;
            node *b = cur->next->next;
            if (a) a->next = b;
            if (b) b->prev = a;
            if (!cur->prev) root = b;
            cur = cur->prev ? cur->prev : b;
        } else {
            cur = cur->next;
        }
    }
    size_t c = 0;
    cur = root;
    while (cur) {
        cur = cur->next;
        c++;
    }
    return c;
}

size_t sol2(const char *line, size_t len) {
    size_t min = SIZE_MAX;
    for (char x = 'A'; x <= 'Z'; x++) {
        char *filtered = malloc(len);
        size_t newlen = 0;
        for (size_t i = 0; i < len; i++) {
            if (line[i] != x && line[i] != x + 32)
                filtered[newlen++] = line[i];
        }
        size_t r = sol1(filtered, newlen);
        min = MIN(min, r);
    }
    return min;
}

int main() {
    char line[50005];
    scanf("%s", line);
    size_t len = strlen(line);
    printf("%zu\n", sol1(line, len));
    printf("%zu\n", sol2(line, len));
    return 0;
}
