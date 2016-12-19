package main


import "bufio"
import "fmt"
import "os"
import "math"

func main() {
    scanner := bufio.NewScanner(os.Stdin)
    x := 1
    y := 1
    for scanner.Scan() {
        line := scanner.Text()
        for _, ch := range line {
            if ch == 'L' {
                x = int(math.Max(0.0, float64(x) - 1))
            } else if ch == 'R' {
                x = int(math.Min(2.0, float64(x) + 1))
            } else if ch == 'U' {
                y = int(math.Max(0.0, float64(y) - 1))
            } else if ch == 'D' {
                y = int(math.Min(2.0, float64(y) + 1))
            }
        }
        fmt.Print(1 + x + y * 3)
    }
    fmt.Println()
}
