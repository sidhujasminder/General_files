package main

import "fmt"

func main() {

	for i := 1; i <= 5; i++ {
		fmt.Printf("This is iteration number %d\n", i)
	}

	// While loop kinda thing.
	i := 1

	for i <= 10 {
		fmt.Println(i)
		i++
	}

}

// execute this file using go run loops.go
