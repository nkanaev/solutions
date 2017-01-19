package main

import "fmt"


func not(x byte) string {
    if x == '0' {
        return "1"
    } else {
        return "0"
    }
}

func extend(input string, max int) string {
    for len(input) < max {
        n := len(input)
        input += "0";
        for i := n - 1; i >= 0; i-- {
            input += not(input[i])
        }
    }
    return input[:max]
}

func checksum(input string) string {
    output := ""
    for i := 0; i < len(input) - 1; i += 2 {
        if input[i] == input[i+1] {
            output += "1"
        } else {
            output += "0"
        }
    }
    return output
}

func main() {
    initial := "01000100010010111"
    maxlength := 272
    result := checksum(extend(initial, maxlength))
    for len(result) % 2 == 0 {
        result = checksum(result)
    }
    fmt.Println(result)
}
