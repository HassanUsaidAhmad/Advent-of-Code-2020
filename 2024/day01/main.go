package main

import (
	"flag"
	"fmt"
)

func main() {
	part := flag.String("part", "1", "Which part do you want to run (1 or 2)")
	flag.Parse()

	switch *part {
	case "1":
		runPart1()
	case "2":
		runPart2()
	default:
		fmt.Println("Invalid part specified. Use -part=1 or -part=2")
	}
}
