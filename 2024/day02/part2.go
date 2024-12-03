package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func checkArr2(arr []int) bool {
	if checkArr(arr) {
		return true
	}

	for i := 0; i < len(arr); i++ {
		// copy before i
		modifiedArr := append([]int{}, arr[:i]...)
		// copy after i
		modifiedArr = append(modifiedArr, arr[i+1:]...)

		if checkArr(modifiedArr) {
			return true
		}
	}
	return false
}

func runPart2() {
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
		arrResult := checkArr2(resultInt)
		if arrResult == true {
			count++
		}
	}
	fmt.Println("Counter: ", count)
}
