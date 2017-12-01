package main


import "fmt"
import "bufio"
import "os"

func main() {
    scanner := bufio.NewScanner(os.Stdin)
    var a, b, c int
    counter := 0
    for scanner.Scan() {
        line := scanner.Text()
        fmt.Sscanf(line, "%d%d%d", &a, &b, &c)
        if a + b > c && a + c > b && b + c > a {
            counter++
        }
    }
    fmt.Println(counter)
}
