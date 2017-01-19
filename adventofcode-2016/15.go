package main

import "fmt"
import "bufio"
import "os"
import "strings"
import "strconv"


type Disc struct {
    num, pos, init int
}


func main() {
    scanner := bufio.NewScanner(os.Stdin)
    discs := make([]Disc, 0)
    for scanner.Scan() {
        words := strings.Split(scanner.Text(), " ")
        num, _ := strconv.Atoi(words[1][1:])
        pos, _ := strconv.Atoi(words[3])
        init, _ := strconv.Atoi(words[11][:len(words[11])-1])
        discs = append(discs, Disc{num: num, pos: pos, init: init})
    }

    for i := 0; true; i++ {
        found := true
        for _, d := range discs {
            if (d.num + d.init + i) % d.pos != 0 {
                found = false
                break
            }
        }
        if found {
            fmt.Println(i)
            break
        }
    }
}
