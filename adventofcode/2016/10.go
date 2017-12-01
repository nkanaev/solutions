package main


import "bufio"
import "os"
import "fmt"
import "strings"
import "strconv"
import "math"

type Bot struct {
    low, high int
    BotLow, BotHigh int
}

func give(bot *Bot, val int) bool {
    if bot.low == 0 {
        bot.low = val
        return false
    } else {
        a, b := float64(bot.low), float64(val)
        bot.low = int(math.Min(a, b))
        bot.high = int(math.Max(a, b))
        return true
    }
}

func main() {
    scanner := bufio.NewScanner(os.Stdin)
    maxBots := 210
    valMin := 17
    valMax := 61
    bots := make([]Bot, maxBots)
    ready := make([]int, 0)

    for i, _ := range bots {
        bots[i].BotLow = -1
        bots[i].BotHigh = -1
    }

    for scanner.Scan() {
        line := scanner.Text()
        words := strings.Split(line, " ");
        if words[0] == "value" {
            val, _ := strconv.Atoi(words[1])
            bot, _ := strconv.Atoi(words[5])
            if give(&bots[bot], val) {
                ready = append(ready, bot)
            }
        } else if words[0] == "bot" {
            bot, _ := strconv.Atoi(words[1])
            low, _ := strconv.Atoi(words[6])
            high, _ := strconv.Atoi(words[11])

            if words[5] == "bot" {
                bots[bot].BotLow = low
            }
            if words[10] == "bot" {
                bots[bot].BotHigh = high
            }
        }
    }

    var i int
    for len(ready) > 0 {
        i, ready = ready[0], ready[1:]  // shift from slice
        if bots[i].BotLow != -1 {
            if give(&bots[bots[i].BotLow], bots[i].low) {
                ready = append(ready, bots[i].BotLow)
            }
        }
        if bots[i].BotHigh != -1 {
            if give(&bots[bots[i].BotHigh], bots[i].high) {
                ready = append(ready, bots[i].BotHigh)
            }
        }
    }
    for i, _ := range bots {
        if bots[i].low == valMin && bots[i].high == valMax {
            fmt.Println(i)
            return
        }
    }
}
