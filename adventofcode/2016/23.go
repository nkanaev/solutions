package main

import "fmt"
import "bufio"
import "os"
import "strings"
import "strconv"


func main() {
    scanner := bufio.NewScanner(os.Stdin)
    ops := make([][]string, 0)
    register := make(map[string]int)
    for scanner.Scan() {
        line := scanner.Text()
        ops = append(ops, strings.Split(line, " "))
    }
    i := 0
    register["a"] = 7
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
        } else if op[0] == "tgl" {
            v := register[op[1]]
            next := i + v
            if next >= len(ops) || next < 0 {
                i += 1
                continue
            }
            if len(ops[next]) == 2 {
                if ops[next][0] == "inc" {
                    ops[next][0] = "dec"
                } else {
                    ops[next][0] = "inc"
                }
            } else if len(ops[next]) == 3 {
                if ops[next][0] == "jnz" {
                    ops[next][0] = "cpy"
                } else {
                    ops[next][0] = "jnz"
                }
            }
            i += 1
        }
    }
    fmt.Println(register["a"])
}
