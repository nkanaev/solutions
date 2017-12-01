package main

import "fmt"
import "bufio"
import "os"
import "strconv"
import "strings"
import "sort"


type Range struct {
    start, end int
}

type Ranges []Range


func (r Ranges) Len() int {
    return len(r)
}


func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}


func (r Ranges) Swap(i, j int) {
    r[i].start, r[j].start = r[j].start, r[i].start
    r[i].end, r[j].end = r[j].end, r[i].end
}


func (r Ranges) Less(i, j int) bool {
    if r[i].start == r[j].start {
        return r[i].end < r[j].end
    }
    return r[i].start < r[j].start
}


func main() {
    scanner := bufio.NewScanner(os.Stdin)
    ranges := make(Ranges, 0)
    for scanner.Scan() {
        line := scanner.Text()
        s := strings.IndexByte(line, '-')
        a, _ := strconv.Atoi(line[0:s])
        b, _ := strconv.Atoi(line[s+1:])
        ranges = append(ranges, Range{a, b})
    }
    sort.Sort(ranges)
    x := ranges[0].end
    for i := 1; i < len(ranges); i++ {
        if x + 1 < ranges[i].start {
            fmt.Println(x + 1)
            break
        } else {
            x = max(x, ranges[i].end)
        }
    }
}
