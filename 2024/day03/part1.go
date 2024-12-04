package main

import (
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
	"strings"
)

// function to convert an array to string
func arrayToString(arr []string) string {
	// seperating string elements with -
	return strings.Join([]string(arr), "-")
}

func runPart1() {
	file, err := os.ReadFile("main.txt")

	if err != nil {
		log.Fatal(err)
	}

	question := string(file)

	m := regexp.MustCompile("mul\\(\\d+,\\d+\\)")

	numbersOnly := m.FindAllString(question, -1)
	numResult := arrayToString(numbersOnly)

	numRe := regexp.MustCompile("\\d+")
	numReArr := numRe.FindAllString(numResult, -1)

	var t2 = []int{}

	for _, i := range numReArr {
		j, err := strconv.Atoi(i)
		if err != nil {
			panic(err)
		}
		t2 = append(t2, j)
	}

	counter := 0

	for i := 0; i < len(t2); i += 2 {
		calc := t2[i] * t2[i+1]
		counter += calc
	}

	fmt.Println(counter)
}
