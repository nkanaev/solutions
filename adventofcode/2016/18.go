package main

import "fmt"


func main() {
    first := "^.^^^.^..^....^^....^^^^.^^.^...^^.^.^^.^^.^^..^.^...^.^..^.^^.^..^.....^^^.^.^^^..^^...^^^...^...^."
    steps := 40
    total := 0

    traps := make([]bool, len(first) + 2)
    for i := 0; i < len(first); i++ {
        if first[i] == '^' {
            traps[i+1] = true
        }
    }

    for i := 0; i < steps; i++ {
        // count traps
        for j := 1; j <= len(first); j++ {
            if !traps[j] {
                total++
            }
        }

        // next row
        nextrow := make([]bool, len(first) + 2)
        for j := 1; j <= len(first); j++ {
            if (traps[j-1] && traps[j] && !traps[j+1]) ||
               (!traps[j-1] && traps[j] && traps[j+1]) ||
               (traps[j-1] && !traps[j] && !traps[j+1]) ||
               (!traps[j-1] && !traps[j] && traps[j+1]) {
                nextrow[j] = true
            }
        }
        traps = nextrow
    }
    fmt.Println(total)
}
