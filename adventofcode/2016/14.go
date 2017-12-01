package main

import "fmt"
import "crypto/md5"
import "strconv"


func three(hash string) (byte, bool) {
    for i := 0; i <= len(hash) - 3; i++ {
        if hash[i] == hash[i+1] && hash[i+1] == hash[i+2] {
            if i != len(hash) - 3 && hash[i+2] == hash[i + 3] {
                continue
            }
            return hash[i], true
        }
    }
    return 0, false
}

func five(hash string, ch byte) bool {
    for i := 0; i <= len(hash) - 5; i++ {
        if hash[i] == ch && hash[i] == hash[i+1] && hash[i+1] == hash[i+2] && 
        hash[i+2] == hash[i+3] && hash[i+3] == hash[i+4] {
            if i != len(hash) - 5 && hash[i + 4] == hash[i + 5] {
                continue
            }
            return true
        }
    }
    return false
}

func hash(salt string, num int) string {
    return fmt.Sprintf("%x", md5.Sum([]byte(salt + strconv.Itoa(num))))
}


func main() {
    salt := "yjdafjpo"
    i := 0
    n := 0
    for {
        ch, found := three(hash(salt, i))
        if found {
            isKey := false
            for j := 1; j < 1000 + 1; j++ {
                if five(hash(salt, i + j), ch) {
                    isKey = true
                    break
                }
            }
            if isKey {
                n += 1
                if n == 64 {
                    fmt.Println(i)
                    return
                }
            }
        }
        i += 1
    }
}
