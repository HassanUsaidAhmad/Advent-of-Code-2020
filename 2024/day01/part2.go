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

func runPart2() {
	file, err := os.Open("main.txt")

	if err != nil {
		log.Fatal(err)
	}

	scanner := bufio.NewScanner(file)

	var leftSide []string
	var rightSide []string
	var ansArr []int

	for scanner.Scan() {
		line := scanner.Text()
		first := strings.Split(line, " ")
		leftSide = append(leftSide, first[0])
		second := line[strings.LastIndex(line, " ")+1:]
		rightSide = append(rightSide, second)
	}

	for _, ls := range leftSide {
		count := 0
		for _, rs := range rightSide {
			if rs == ls {
				count++
			}
		}

		leftInt, _ := strconv.Atoi(ls)
		ansArr = append(ansArr, count*leftInt)
	}

	finalResult := utils.ArraySum(ansArr)
	fmt.Println(finalResult)
}
