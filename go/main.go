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

func solve002() int {
	s := 0
	var fib []int
	fib = append(fib, 1)
	fib = append(fib, 2)
	for fib[len(fib)-1] < 4000000 {
		fib = append(fib, fib[len(fib)-1]+fib[len(fib)-2])
	}
	fib = fib[:len(fib)-1]
	for _, val := range fib {
		if val%2 == 0 {
			s += val
		}
	}
	return s
}

func main() {
	arg := os.Args[1]
	switch arg {
	case "1":
		fmt.Println(solve001())
	case "2":
		fmt.Println(solve002())
	default:
		fmt.Println("NA")
	}
}
