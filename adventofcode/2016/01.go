package main

import "fmt"
import "strconv"
import "os"
import "bufio"
import "strings"
import "math"


func main() {
    reader := bufio.NewReader(os.Stdin)
    line, _, _ := reader.ReadLine()
    x := 0
    y := 0
    px := 0
    py := 1
    t := 0

    movements := strings.Split(string(line), ", ")
    for _, move := range movements {
        t = px
        if move[0] == 'L' {
            px = -py
            py = t
        } else {
            px = py
            py = -t
        }
        n, _ := strconv.Atoi(string(move[1:]))
        x = x + n * px
        y = y + n * py
    }
    fmt.Println(math.Abs(float64(x)) + math.Abs(float64(y)))
}

