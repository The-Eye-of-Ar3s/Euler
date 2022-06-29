package main

import (
	"fmt"
	"os"
	"strconv"
)

func reverse(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

func prime_factorize(n int) []int {
	var r []int
	p := 2
	for n >= p*p {
		if n%p == 0 {
			r = append(r, p)
			n /= p
		} else {
			p += 1
		}
	}
	r = append(r, n)
	return r
}

func is_palindrome(n int) bool {
	s := strconv.Itoa(n)
	r := reverse(s)
	return s == r
}

func is_prime(n int) bool {
	if n == 1 {
		return false
	}
	i := 2
	for i*i <= n {
		if n%i == 0 {
			return false
		}
		i += 1
	}
	return true
}

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

func solve003() int {
	pf := prime_factorize(600851475143)
	return pf[len(pf)-1]
}

func solve004() int {
	m := 0
	ml := 0
	for i := 999; i > 100; i -= 1 {
		for j := i; j > 100; j -= 1 {
			ml = i * j
			if is_palindrome(ml) && ml > m {
				m = ml
			}
		}
	}
	return m
}

func solve006() int {
	n1 := 0
	n2 := 0
	for i := 1; i <= 100; i += 1 {
		n1 += i * i
		n2 += i
	}
	n2 *= n2
	return n2 - n1
}

func solve007() int {
	var p []int
	i := 3
	p = append(p, 2)
	for len(p) != 10001 {
		if is_prime(i) {
			p = append(p, i)
		}
		i += 2
	}
	return p[10000]
}

func main() {
	arg := os.Args[1]
	switch arg {
	case "1":
		fmt.Println(solve001())
	case "2":
		fmt.Println(solve002())
	case "3":
		fmt.Println(solve003())
	case "4":
		fmt.Println(solve004())
	case "6":
		fmt.Println(solve006())
	case "7":
		fmt.Println(solve007())
	default:
		fmt.Println("NA")
	}
}
