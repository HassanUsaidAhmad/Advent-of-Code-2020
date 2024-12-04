package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func runPart1() {
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

	for i := 0; i < len(lines); i++ {
		for j := 0; j <= len(lines[i])-4; j++ {
			// Checking for XMAS Horizontally
			if string(lines[i][j]) == "X" && string(lines[i][j+1]) == "M" && string(lines[i][j+2]) == "A" && string(lines[i][j+3]) == "S" {
				counter += 1
			}
			// Checking for SAMX Horizontally
			if string(lines[i][j]) == "S" && string(lines[i][j+1]) == "A" && string(lines[i][j+2]) == "M" && string(lines[i][j+3]) == "X" {
				counter += 1
			}
		}
	}

	for i := 3; i < len(lines); i++ {
		for j := 0; j < len(lines[i]); j++ {
			// Checking for SAMX Vertically
			if string(lines[i][j]) == "X" && string(lines[i-1][j]) == "M" && string(lines[i-2][j]) == "A" && string(lines[i-3][j]) == "S" {
				counter += 1
			}
			// Checking for XMAS Vertically
			if string(lines[i][j]) == "S" && string(lines[i-1][j]) == "A" && string(lines[i-2][j]) == "M" && string(lines[i-3][j]) == "X" {
				counter += 1
			}
		}
		for a := 3; a < len(lines[i-3]); a++ {
			// Check Diagnal XMAS
			if string(lines[i-3][a]) == "S" && string(lines[i-2][a-1]) == "A" && string(lines[i-1][a-2]) == "M" && string(lines[i][a-3]) == "X" {
				counter += 1
			}
			// Check Diagnal XMAS
			if string(lines[i-3][a]) == "X" && string(lines[i-2][a-1]) == "M" && string(lines[i-1][a-2]) == "A" && string(lines[i][a-3]) == "S" {
				counter += 1
			}
		}
		for b := 3; b < len(lines[i]); b++ {
			// Check Diagnal XMAS
			if string(lines[i][b]) == "S" && string(lines[i-1][b-1]) == "A" && string(lines[i-2][b-2]) == "M" && string(lines[i-3][b-3]) == "X" {
				counter += 1
			}
			// Check Diagnal XMAS
			if string(lines[i][b]) == "X" && string(lines[i-1][b-1]) == "M" && string(lines[i-2][b-2]) == "A" && string(lines[i-3][b-3]) == "S" {
				counter += 1
			}
		}
	}
	fmt.Println(counter)
}
