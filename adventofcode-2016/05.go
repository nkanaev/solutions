package main


import "fmt"
import "bufio"
import "os"
import "crypto/md5"
import "strconv"

func main() {
    reader := bufio.NewReader(os.Stdin)
    line, _, _ := reader.ReadLine()
    id := string(line)

    result := make([]byte, 0)
    for i := 0;; i++ {
        hash := fmt.Sprintf("%x", md5.Sum([]byte(id + strconv.Itoa(i))))
        if hash[0:5] == "00000" {
            result = append(result, hash[5])
        }
        if len(result) == 8 {
            break
        }
    }
    fmt.Println(string(result))
}
