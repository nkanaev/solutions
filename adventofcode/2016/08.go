package main


import "fmt"
import "bufio"
import "os"
import "strings"
import "strconv"

func main() {
    scanner := bufio.NewScanner(os.Stdin)
    w := 50
    h := 6
    var screen [50][6]bool
    for scanner.Scan() {
        cmd := strings.Split(scanner.Text(), " ")
        if cmd[0] == "rect" {
            size := strings.Split(cmd[1], "x")
            w, _ := strconv.Atoi(size[0])
            h, _ := strconv.Atoi(size[1])
            for x := 0; x < w; x++ {
                for y := 0; y < h; y++ {
                    screen[x][y] = true
                }
            }
        } else if cmd[0] == "rotate" {
            if cmd[1] == "column" {
                x, _ := strconv.Atoi(strings.Split(cmd[2], "=")[1])
                r, _ := strconv.Atoi(cmd[4])
                r = r % h
                for i := 0; i < (h - r) / 2; i++ {
                    screen[x][i], screen[x][h-r-1-i] = screen[x][h-r-1-i], screen[x][i]
                }
                for i := 0; i < r / 2; i++ {
                    screen[x][h-r+i], screen[x][h-1-i] = screen[x][h-1-i], screen[x][h-r+i]
                }
                for i := 0; i < h / 2; i++ {
                    screen[x][i], screen[x][h-1-i] = screen[x][h-1-i], screen[x][i]
                }
            } else if cmd[1] == "row" {
                y, _ := strconv.Atoi(strings.Split(cmd[2], "=")[1])
                r, _ := strconv.Atoi(cmd[4])
                r = r % w
                for i := 0; i < (w - r) / 2; i++ {
                    screen[i][y], screen[w-r-1-i][y] = screen[w-r-1-i][y], screen[i][y]
                }
                for i := 0; i < r / 2; i++ {
                    screen[w-r+i][y], screen[w-1-i][y] = screen[w-1-i][y], screen[w-r+i][y]
                }
                for i := 0; i < w / 2; i++ {
                    screen[i][y], screen[w-1-i][y] = screen[w-1-i][y], screen[i][y]
                }
            }
        }
    }

    counter := 0
    for y := 0; y < h; y++ {
        for x := 0; x < w; x++ {
            if screen[x][y] {
                counter++
            }
        }
    }
    fmt.Println(counter)
}
