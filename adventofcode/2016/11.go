package main

import "fmt"
import "strconv"


type State struct {
    step, current int
    floors []uint
}


func safe(floors []uint, pairs uint) bool {
    for _, f := range floors {
        leftrtg := 0
        leftchp := 0
        var i uint
        for i = 0; i < pairs * 2; i += 2 {
            if (f & (1 << i)) != 0 && (f & (1 << (i + 1))) != 0 {
                continue
            } else if (f & (1 << i)) != 0 && (f ^ (1 << (i + 1))) != 0 {
                leftchp++
            } else if (f ^ (1 << i)) != 0 && (f & (1 << (i + 1))) != 0 {
                leftrtg++
            }
        }
        if leftrtg > 0 && leftchp > 0 {
            return false
        }
    }
    return true
}


func bin2uint(s string) uint {
    x, _ := strconv.ParseInt(s, 2, 0)
    return uint(x)
}


func main() {
    initial := make([]uint, 4)
    //initial[0] = bin2uint("0101")
    //initial[1] = bin2uint("1000")
    //initial[2] = bin2uint("0010")
    //pairs := uint(2)
    initial[0] = bin2uint("1011101111")
    initial[1] = bin2uint("0100010000")
    pairs := uint(5)

    queue := make([]State, 0)
    queue = append(queue, State{0, 0, initial})
    seen := make(map[string]bool, 0)
    for len(queue) > 0 {
        state := queue[0]
        queue = queue[1:]
        step := state.step
        floors := state.floors
        current := state.current

        hash := fmt.Sprintf("%d|%d|%d|%d|%d",
            floors[0], floors[1], floors[2], floors[3], current)
        if seen[hash] == true {
            continue
        } else {
            seen[hash] = true
        }

        if !safe(floors, pairs) {
            continue
        }

        if floors[current] & 85 == 0 {
            continue
        }

        if current == len(floors) - 1 {
            x := floors[len(floors) - 1]
            if x + 1 == 1 << (pairs * 2) {
                fmt.Println(step)
                break
            }
        }

        var a, b, v uint
        for a = 0; a < pairs * 2; a++ {
            for b = a; b < pairs * 2; b++ {
                v = (1 << uint(a)) | (1 << uint(b))
                if floors[current] & v != v {
                    continue
                }

                if current < len(floors) - 1 {
                    nfloor := append([]uint(nil), floors...)
                    nfloor[current] ^=  v
                    nfloor[current + 1] ^= v
                    queue = append(queue, State{step + 1, current + 1, nfloor})
                }
                if current > 0 {
                    if current == 1 && floors[0] == 0 {
                        continue
                    }
                    if current == 2 && floors[0] == 0 && floors[1] == 0 {
                        continue
                    }

                    nfloor := append([]uint(nil), floors...)
                    nfloor[current] ^=  v
                    nfloor[current - 1] ^= v
                    queue = append(queue, State{step + 1, current - 1, nfloor})
                }
            }
        }
    }
}
