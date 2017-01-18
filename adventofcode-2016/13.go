package main

import "fmt"
import "math"


func popcount(input uint64) uint8 {
    var mask1, mask2, mask3, mask4, mask5, mask6 uint64
    mask1 = 6148914691236517205 // 01010101...
    mask2 = 3689348814741910323 // 00110011...
    mask3 = 1085102592571150095 // 00001111...
    mask4 = 71777214294589695   // 8 zeroes, 8 ones, etc...
    mask5 = 70367670468607      // 16 zeroes, 16 ones, etc...
    mask6 = 4294967295          // 32 zeroes, 32 ones

    input = (input & mask1) + ((input >> 1) & mask1)
    input = (input & mask2) + ((input >> 2) & mask2)
    input = (input & mask3) + ((input >> 4) & mask3)
    input = (input & mask4) + ((input >> 8) & mask4)
    input = (input & mask5) + ((input >> 16) & mask5)
    input = (input & mask6) + ((input >> 32) & mask6)

    return uint8(input)
}

func openspace(x, y int, a int) bool {
    if x < 0 || y < 0 {
        return false
    }
    return popcount(uint64(x*x + 3*x + 2*x*y + y + y*y + a)) % 2 == 0
}

type Point struct {
    x, y int
}

func main() {
    m := [100][100]int{}
    fav := 1352
    dest := Point{x: 31, y: 39}
    queue := make([]Point, 0)
    queue = append(queue, Point{x: 1, y: 1})
    var p Point
    for len(queue) != 0 {
        p, queue = queue[0], queue[1:]
        if p.x == dest.x && p.y == dest.y {
            break
        }

        points := make([]Point, 0)
        if openspace(p.x + 1, p.y, fav) {
            points = append(points, Point{x: p.x + 1, y: p.y})
        }
        if openspace(p.x - 1, p.y, fav) {
            points = append(points, Point{x: p.x - 1, y: p.y})
        }
        if openspace(p.x, p.y + 1, fav) {
            points = append(points, Point{x: p.x, y: p.y + 1})
        }
        if openspace(p.x, p.y - 1, fav) {
            points = append(points, Point{x: p.x, y: p.y - 1})
        }

        for _, a := range points {
            if m[a.x][a.y] != 0 {
                m[a.x][a.y] = int(math.Min(
                    float64(m[p.x][p.y] + 1),
                    float64(m[a.x][a.y])))
            } else {
                queue = append(queue, a)
                m[a.x][a.y] = m[p.x][p.y] + 1
            }
        }
    }
    fmt.Println(m[dest.x][dest.y])
}
