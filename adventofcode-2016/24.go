package main

import "fmt"
import "bufio"
import "os"
import "strconv"


type Point struct {
    col, row int
}


func shortest(maze []string, a, b Point) int {
    return 1
}


func main() {
    scanner := bufio.NewScanner(os.Stdin)
    maze := make([]string, 0)
    points := make([]Point, 10)
    col := 0
    max := 0
    for scanner.Scan() {
        line := scanner.Text()
        maze = append(maze, line)
        for row, c := range line {
            if '0' <= c && c <= '9' {
                i, _ := strconv.Atoi(string(c))
                points[i] = Point{col, row}
                if i > max {
                    max = i
                }
            }
        }
        col++
    }

    shortest := [10][10]int{}
    for current_point := 0; current_point <= max; current_point++ {
        distance := make([][]int, len(maze))
        for i := 0; i < len(maze); i++ {
            distance[i] = make([]int, len(maze[i]))
        }
        found := max
        queue := make([]Point, 0)
        queue = append(queue, points[current_point])
        var p Point
        next := [][]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
        for found > 0 {
            p, queue = queue[0], queue[1:]
            for _, n := range next {
                col2, row2 := p.col + n[0], p.row + n[1]
                if col2 == points[current_point].col &&
                   row2 == points[current_point].row {
                    continue
                }
                ch := maze[col2][row2]
                if ch == '#' {
                    continue
                }
                if distance[col2][row2] != 0 {
                    continue
                }

                distance[col2][row2] = distance[p.col][p.row] + 1
                queue = append(queue, Point{col2, row2})

                if '0' <= ch && ch <= '9' {
                    found_point := ch - '0'
                    shortest[current_point][found_point] = distance[col2][row2]
                    found--
                }
            }
        }
    }

    idxs := make([]int, max)
    for i := 1; i <= max; i++ {
        idxs[i-1] = i
    }
    min_distance := 1 << 31 - 1
    var perm func([]int, int)
    perm = func(a []int, size int) {
        if size == 1 {
            total_distance := shortest[0][a[0]]
            for i := 0; i < len(a) - 1; i++ {
                total_distance += shortest[a[i]][a[i+1]]
            }
            if total_distance < min_distance {
                min_distance = total_distance
            }
            return
        }

        for i := 0; i < size; i++ {
            perm(a, size - 1)

            if size % 2 == 1 {
                a[0], a[size - 1] = a[size - 1], a[0]
            } else {
                a[i], a[size - 1] = a[size - 1], a[i]
            }
        }
    }
    perm(idxs, len(idxs))
    fmt.Println(min_distance)
}
