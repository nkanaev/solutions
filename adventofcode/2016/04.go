package main


import "fmt"
import "bufio"
import "os"
import "regexp"
import "strconv"
import "strings"
import "sort"
import "bytes"


type CharFreq struct {
    char int
    freq int
}


type ByFreq []CharFreq;

func (s ByFreq) Len() int {
    return len(s)
}
func (s ByFreq) Swap(i, j int) {
    s[i].char, s[j].char = s[j].char, s[i].char
    s[i].freq, s[j].freq = s[j].freq, s[i].freq
}
func (s ByFreq) Less(i, j int) bool {
    return s[i].freq < s[j].freq
}


func main() {
    sum := 0
    scanner := bufio.NewScanner(os.Stdin)
    r := regexp.MustCompile("([a-z|-]+)-([0-9]+)\\[([a-z]+)\\]")
    for scanner.Scan() {
        m := make([]CharFreq, 26);
        for i := 0; i < 26; i++ {
            m[i] = CharFreq{i, 0}
        }

        line := scanner.Text()
        match := r.FindStringSubmatch(line)

        name := strings.Replace(match[1], "-", "", -1)
        sid, _ := strconv.Atoi(match[2])
        checksum := match[3]

        for _, ch := range name {
            m[ch - 'a'].freq += 1
        }

        sort.Stable(sort.Reverse(ByFreq(m)))
        var bf bytes.Buffer
        for i := 0; i < 5; i++ {
            bf.WriteByte(byte(m[i].char + 'a'))
        }
        if checksum == bf.String() {
            sum += sid
        }
    }
    fmt.Println(sum)
}
