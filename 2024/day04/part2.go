package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func runPart2() {
	file, err := os.Open("main.txt")

	if err != nil {
		log.Fatal(err)
	}

	scanner := bufio.NewScanner(file)
	counter := 0

	lines := []string{}

	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	for i := 2; i < len(lines); i++ {
		for a := 2; a < len(lines[i]); a++ {
			// Check Diagnal XMAS
			if string(lines[i][a]) == "S" && string(lines[i-1][a-1]) == "A" && string(lines[i-2][a-2]) == "M" && string(lines[i][a-2]) == "M" && string(lines[i-2][a]) == "S" {
				counter += 1
			}
			// Check Diagnal XMAS
			if string(lines[i][a]) == "M" && string(lines[i-1][a-1]) == "A" && string(lines[i-2][a-2]) == "S" && string(lines[i][a-2]) == "S" && string(lines[i-2][a]) == "M" {
				counter += 1
			}
			// Check Diagnal XMAS
			if string(lines[i][a]) == "M" && string(lines[i-1][a-1]) == "A" && string(lines[i-2][a-2]) == "S" && string(lines[i][a-2]) == "M" && string(lines[i-2][a]) == "S" {
				counter += 1
			}
			// Check Diagnal XMAS
			if string(lines[i][a]) == "S" && string(lines[i-1][a-1]) == "A" && string(lines[i-2][a-2]) == "M" && string(lines[i][a-2]) == "S" && string(lines[i-2][a]) == "M" {
				counter += 1
			}
		}
	}
	fmt.Println(counter)
}

