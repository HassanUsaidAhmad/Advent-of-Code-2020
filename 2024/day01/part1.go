package main

import (
	"advent-of-code/utils"
	"bufio"
	"fmt"
	"log"
	"math"
	"os"
	"sort"
	"strconv"
	"strings"
)

func runPart1() {
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

	sort.Sort(sort.StringSlice(leftSide))
	sort.Sort(sort.StringSlice(rightSide))

	for i := range leftSide {
		leftInt, _ := strconv.Atoi(leftSide[i])
		rightInt, _ := strconv.Atoi(rightSide[i])
		result := math.Abs(float64(leftInt) - float64(rightInt))
		ansArr = append(ansArr, int(result))
	}

	finalResult := utils.ArraySum(ansArr)
	fmt.Println(finalResult)
}
