package main

import "math"
import "fmt"


func main() {
    x := 3005290
    // The Josephus Problem
    fmt.Println(((x ^ (1 << uint(math.Log2(float64(x))))) << 1) + 1)
}
