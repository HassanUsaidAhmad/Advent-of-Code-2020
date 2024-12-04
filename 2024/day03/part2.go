package main

import (
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func runPart2() {
	file, err := os.ReadFile("main.txt")

	if err != nil {
		log.Fatal(err)
	}

	question := string(file)

	m := regexp.MustCompile(`do\(\)|don't\(\)|mul\(\d+,\d+\)`)
	doMul := m.FindAllString(question, -1)

	enabled := true
	counter := 0

	for _, token := range doMul {
		if token == "do()" {
			enabled = true
		} else if token == "don't()" {
			enabled = false
		} else if strings.HasPrefix(token, "mul") && enabled {
			numRe := regexp.MustCompile(`\d+`)
			numReArr := numRe.FindAllString(token, -1)
			x, _ := strconv.Atoi(numReArr[0])
			y, _ := strconv.Atoi(numReArr[1])
			counter += x * y
		}
	}

	fmt.Println(counter)
}
