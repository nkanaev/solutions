#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define shortcmp(a, b, field) if (a->field != b->field) return a->field - b->field;

typedef struct {
    int year, month, day;
    int hour, min;
    int guard;
    char statusline[30];
    enum { S_STARTSHIFT, S_ASLEEP, S_WAKEUP } status;
} record;

int compare_records(const void *a, const void *b) {
    record *r1 = (record*)a;
    record *r2 = (record*)b;

    shortcmp(r1, r2, year)
    shortcmp(r1, r2, month)
    shortcmp(r1, r2, day)
    shortcmp(r1, r2, hour)
    shortcmp(r1, r2, min)

    return 0;
}

int sol1(record *records, size_t count) {
    int total_asleep[4000];
    for (size_t i = 0; i < 4000; i++)
        total_asleep[i] = 0;

    int chosen = 0;
    size_t sleeping_idx = 0;
    for (size_t i = 0; i < count; i++) {
        if (records[i].status == S_ASLEEP) {
            sleeping_idx = i;
        } else if (records[i].status == S_WAKEUP) {
            if (records[i].guard == records[sleeping_idx].guard) {
                int asleep = records[i].min - records[sleeping_idx].min;
                total_asleep[records[i].guard] += asleep;

                if (total_asleep[records[i].guard] > total_asleep[chosen]) {
                    chosen = records[i].guard;
                }
            }
        }
    }

    int startmin = 0;
    int asleep[60];
    for (int i = 0; i < 60; i++)
        asleep[i] = 0;
    for (size_t i = 0; i < count; i++) {
        if (records[i].guard != chosen)
            continue;
        if (records[i].status == S_ASLEEP) {
            startmin = records[i].min;
        } else if (records[i].status == S_WAKEUP) {
            for (int j = startmin; j < records[i].min; j++)
                asleep[j]++;
        }
    }

    int bestmin = 0;
    for (int i = 0; i < 60; i++)
        if (asleep[i] > asleep[bestmin])
            bestmin = i;

    return chosen * bestmin;
}

int sol2(record *records, size_t count) {
    int sleep_counter[4000][60];
    int guard, startmin;

    for (int i = 0; i < 4000 * 60; i++)
        sleep_counter[i / 60][i % 60] = 0;

    for (size_t row = 0; row < count; row++) {
        switch (records[row].status) {
            case S_STARTSHIFT:
                guard = records[row].guard;
                break;
            case S_ASLEEP:
                startmin = records[row].min;
                break;
            case S_WAKEUP:
                for (int min = startmin; min < records[row].min; min++)
                    sleep_counter[guard][min]++;
                break;
        }
    }
    int chosen = 0, bestmin = 0;
    for (int c = 0; c < 4000 ; c++)
        for (int m = 0; m < 60; m++)
            if (sleep_counter[c][m] > sleep_counter[chosen][bestmin]) {
                chosen = c;
                bestmin = m;
            }
    return chosen * bestmin;
}

int main() {
    record records[2000];
    size_t count;
    while (1) {
        size_t i = count;
        int result = scanf(
            "[%d-%d-%d %d:%d] %[^\n]\n",
            &(records[i].year), &(records[i].month), &(records[i].day),
            &(records[i].hour), &(records[i].min), records[i].statusline);
        if (result == EOF)
            break;
        count++;
    }

    qsort(records, count, sizeof(record), compare_records);

    int currentGuard = -1;
    char *line;

    for (size_t i = 0; i < count; i++) {
        line = records[i].statusline;
        if (strncmp(line, "Guard", 5) == 0) {
            sscanf(line, "Guard #%d", &currentGuard);
            records[i].status = S_STARTSHIFT;
        } else if (strncmp(line, "falls asleep", 12) == 0) {
            records[i].status = S_ASLEEP;
        } else if (strncmp(line, "wakes up", 8) == 0) {
            records[i].status = S_WAKEUP;
        }
        records[i].guard = currentGuard;
    }

    printf("%d\n", sol1(records, count));
    printf("%d\n", sol2(records, count));
    return 0;
}
