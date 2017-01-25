package main

import "fmt"
import "bufio"
import "os"
import "strings"
import "strconv"


func main() {
    scanner := bufio.NewScanner(os.Stdin)
    ops := make([][]string, 0)
    for scanner.Scan() {
        line := scanner.Text()
        ops = append(ops, strings.Split(line, " "))
    }
    threshold := 1000

Reset:
    for n := 0; true; n++ {
        i := 0
        register := make(map[string]int)
        register["a"] = n
        signals := make([]int, 0)
        for i < len(ops) {
            op := ops[i]
            if op[0] == "cpy" {
                if _, ok := register[op[1]]; ok {
                    register[op[2]] = register[op[1]]
                } else {
                    x, _ := strconv.Atoi(op[1])
                    register[op[2]] = x
                }
                i += 1
            } else if op[0] == "inc" {
                register[op[1]] += 1
                i += 1
            } else if op[0] == "dec" {
                register[op[1]] -= 1
                i += 1
            } else if op[0] == "jnz" {
                v := 0
                if _, ok := register[op[1]]; ok {
                    v = register[op[1]]
                } else {
                    v, _ = strconv.Atoi(op[1])
                }
                if v != 0 {
                    x := 0
                    if _, ok := register[op[2]]; ok {
                        x = register[op[2]]
                    } else {
                        x, _ = strconv.Atoi(op[2])
                    }
                    i += x
                } else {
                    i += 1
                }
            } else if op[0] == "out" {
                signals = append(signals, register[op[1]])
                i += 1

                if len(signals) > 1 {
                    if signals[len(signals) - 1] == signals[len(signals) - 2] {
                        continue Reset
                    }
                }

                if len(signals) >= threshold {
                    fmt.Println(n)
                    return
                }
            }
        }
    }
}
