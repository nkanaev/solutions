package main


import "fmt"
import "bufio"
import "os"


func tokens(input string) ([]string, []string) {
    open := make([]string, 0)
    closed := make([]string, 0)
    chunk := make([]rune, 0)
    for _, ch := range input {
        if ch == '[' {
            open = append(open, string(chunk))
            chunk = make([]rune, 0)
        } else if ch == ']' {
            closed = append(closed, string(chunk))
            chunk = make([]rune, 0)
        } else {
            chunk = append(chunk, ch)
        }
    }
    open = append(open, string(chunk))
    return open, closed
}


func abba(input string) bool {
    for i := 0; i < len(input) - 3; i++ {
        if input[i] != input[i+1] && input[i] == input[i+3] && input[i+1] == input[i+2] {
            return true
        }
    }
    return false
}


func main() {
    scanner := bufio.NewScanner(os.Stdin)
    counter := 0

    SCAN:
    for scanner.Scan() {
        line := scanner.Text()
        open, closed := tokens(line)
        for _, c := range closed {
            if abba(c) {
                continue SCAN
            }
        }
        for _, c := range open {
            if abba(c) {
                counter++
                continue SCAN
            }
        }
    }
    fmt.Println(counter)
}
