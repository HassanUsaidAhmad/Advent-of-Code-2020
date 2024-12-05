package main

import (
	"advent-of-code/utils"
	"bufio"
	"fmt"
	"log"
	"os"
	"slices"
	"strconv"
	"strings"
)

func sortSequence(sequence []string, rulesMap map[string][]string) []string {
	for i := 0; i < len(sequence)-1; i++ {
		for j := 0; j < len(sequence)-1; j++ {
			allowedNext, exists := rulesMap[sequence[j]]
			if exists && !slices.Contains(allowedNext, sequence[j+1]) {
				sequence[j], sequence[j+1] = sequence[j+1], sequence[j]
			}
		}
	}
	return sequence
}

func runPart2() {
	file, err := os.Open("main.txt")

	if err != nil {
		log.Fatal(err)
	}

	scanner := bufio.NewScanner(file)
	w := true
	rules := []string{}
	pages := []string{}
	rulesMap := make(map[string][]string)

	for scanner.Scan() {
		lines := scanner.Text()
		if lines == "" {
			w = false
		}
		if w == true {
			result := strings.Split(lines, "|")
			rules = append(rules, utils.ArrayToString(result))
		} else if w == false {
			pages = append(pages, lines)
		}
	}

	for _, rule := range rules {
		side := strings.Split(rule, " ")
		key := side[0]
		value := side[1]
		rulesMap[key] = append(rulesMap[key], value)
	}

	middleNumber := []string{}

	for i := 1; i < len(pages); i++ {
		result := strings.Split(pages[i], ",")
		counter := 0
		for j := 1; j <= len(result)-1; j++ {
			val, _ := rulesMap[result[j-1]]
			isContain := slices.Contains(val, string(result[j]))
			if !isContain {
				counter++
			}
		}
		if counter == 0 {
			continue
		} else if counter != 0 {
			sorted := sortSequence(result, rulesMap)
			middle := len(sorted) / 2
			middleNumber = append(middleNumber, sorted[middle])
		}
	}

	var t2 = []int{}

	for _, i := range middleNumber {
		j, err := strconv.Atoi(i)
		if err != nil {
			panic(err)
		}
		t2 = append(t2, j)
	}
	final := utils.ArraySum(t2)
	fmt.Println(final)
}

