package main

import (
	"advent-of-code/utils"
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func checkArr(arr []int) bool {
	var incOrDec string
	number := 1
	if arr[number] > arr[number-1] {
		incOrDec = "inc"
	} else {
		incOrDec = "dec"
	}
	for number <= len(arr)-1 {
		calc := utils.Absolute((arr[number] - arr[number-1]))
		if calc == 0 {
			return false
		} else if calc > 3 {
			return false
		} else if incOrDec == "inc" && arr[number] > arr[number-1] {
			number++
		} else if incOrDec == "dec" && arr[number] < arr[number-1] {
			number++
		} else {
			return false
		}
	}
	return true
}

func runPart1() {
	file, err := os.Open("main.txt")

	if err != nil {
		log.Fatal(err)
	}

	scanner := bufio.NewScanner(file)
	count := 0

	for scanner.Scan() {
		line := scanner.Text()
		result := strings.Split(line, " ")
		var resultInt = []int{}
		for _, i := range result {
			j, err := strconv.Atoi(i)
			if err != nil {
				panic(err)
			}
			resultInt = append(resultInt, j)
		}
		arrResult := checkArr(resultInt)
		if arrResult == true {
			count++
		}
	}
	fmt.Println("Counter: ", count)
}
