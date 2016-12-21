package main


import "fmt"
import "bufio"
import "os"
import "strings"
import "strconv"

func main() {
    reader := bufio.NewReader(os.Stdin)
    line, _ := reader.ReadString('\n')

    i := 0
    c := int64(0)
    fmt.Println("length", len(line))
    for i < len(line) {
        if line[i] == '(' {
            x := i + 1
            for line[i] != ')' {
                i++
            }
            fmt.Println(string(line[x:i]))
            nums := strings.Split(string(line[x:i]), "x")
            offset, _ := strconv.Atoi(nums[0])
            times, _ := strconv.Atoi(nums[1])
            i += offset + 1
            c += int64(offset * times)
        } else {
            if line[i] != '\n' && line[i] != ' ' {
                c++
            }
            i++
        }
    }
    fmt.Println(c)
}
