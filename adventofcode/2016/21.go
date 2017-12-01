package main

import "fmt"
import "bufio"
import "os"
import "strings"
import "strconv"
import "bytes"


func main() {
    input := "abcdefgh"
    x := []byte(input)
    scanner := bufio.NewScanner(os.Stdin)
    for scanner.Scan() {
        line := scanner.Text()
        cmd := strings.Split(line, " ")
        if cmd[0] == "swap" && cmd[1] == "position" {
            i, _ := strconv.Atoi(cmd[2])
            j, _ := strconv.Atoi(cmd[5])
            x[i], x[j] = x[j], x[i]
        } else if cmd[0] == "swap" && cmd[1] == "letter" {
            i := bytes.IndexByte(x, cmd[2][0])
            j := bytes.IndexByte(x, cmd[5][0])
            x[i], x[j] = x[j], x[i]
        } else if cmd[0] == "reverse" {
            i, _ := strconv.Atoi(cmd[2])
            j, _ := strconv.Atoi(cmd[4])
            for i < j {
                x[i], x[j] = x[j], x[i]
                i += 1
                j -= 1
            }
        } else if cmd[0] == "rotate" && (cmd[1] == "left" || cmd[1] == "right") {
            i, _ := strconv.Atoi(cmd[2])
            if cmd[1] == "right" {
                i = len(x) - i
            }
            x = append(x[i:], x[:i]...)
        } else if cmd[0] == "move" && cmd[1] == "position" {
            i, _ := strconv.Atoi(cmd[2])
            j, _ := strconv.Atoi(cmd[5])
            if i < j {
                ch := x[i]
                for n := i; n < j; n++ {
                    x[n] = x[n + 1]
                }
                x[j] = ch
            } else {
                ch := x[i]
                for n := i; n > j; n-- {
                    x[n] = x[n - 1]
                }
                x[j] = ch
            }
        } else if cmd[0] == "rotate" && cmd[1] == "based" {
            i := bytes.IndexByte(x, cmd[6][0])
            if i >= 4 {
                i++
            }
            i = len(x) - ((i + 1) % len(x))
            x = append(x[i:], x[:i]...)
        }
    }
    fmt.Println(string(x))
}
