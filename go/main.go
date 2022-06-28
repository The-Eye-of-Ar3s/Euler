package main

import (
	"fmt"
	"os"
)

func solve001() int {
	s := 0
	for i := 1; i < 1000; i++ {
		if i%3 == 0 || i%5 == 0 {
			s += i
		}
	}
	return s
}

func main() {
	arg := os.Args[1]
	switch arg {
	case "1":
		fmt.Println(solve001())
	default:
		fmt.Println("NA")
	}
}
