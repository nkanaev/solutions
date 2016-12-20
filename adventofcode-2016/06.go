package main


import "bufio"
import "fmt"
import "os"

func most_common_char(messages []string, pos int) byte {
    var chars [26]byte;
    for _, message := range messages {
        chars[message[pos] - 'a']++
    }
    m := 0
    for i := 1; i < 26; i++ {
        if chars[i] > chars[m] {
            m = i
        }
    }
    return byte(m) + 'a'
}

func main() {
    scanner := bufio.NewScanner(os.Stdin)

    messages := make([]string, 0)
    for scanner.Scan() {
        messages = append(messages, scanner.Text())
    }

    out := make([]byte, 8)
    for i := 0; i < 8; i++ {
        out[i] = most_common_char(messages, i)
    }
    fmt.Println(string(out))
}
