package main

import "fmt"
import "crypto/md5"


func openpath(x byte) bool {
    return !('0' <= x && x <= '9')
}


type PathState struct {
    val string
    x, y int
}


func main() {
    key := "lpvhkcbi"
    queue := make([]PathState, 1)
    queue[0] = PathState{key, 0, 0}
    var c PathState
    for len(queue) > 0 {
        c, queue = queue[0], queue[1:]

        if c.x == 3 && c.y == 3 {
            fmt.Println(c.val[len(key):])
            break
        }

        hash := fmt.Sprintf("%x", md5.Sum([]byte(c.val)))

        // up
        if openpath(hash[0]) && c.y > 0 {
            queue = append(queue, PathState{c.val + "U", c.x, c.y - 1})
        }
        // down
        if openpath(hash[1]) && c.y < 3 {
            queue = append(queue, PathState{c.val + "D", c.x, c.y + 1})
        }
        // left
        if openpath(hash[2]) && c.x > 0 {
            queue = append(queue, PathState{c.val + "L", c.x - 1, c.y})
        }
        // right
        if openpath(hash[3]) && c.x < 3 {
            queue = append(queue, PathState{c.val + "R", c.x + 1, c.y})
        }
    }
}
