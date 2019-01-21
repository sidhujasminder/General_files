package main

import "fmt"

func main() {

	var evennum [5]int
	evennum[0] = 0
	evennum[1] = 2
	evennum[2] = 4
	evennum[3] = 6
	evennum[4] = 8

	for i := 0; i < 5; i++ {
		fmt.Println(evennum[i])
	}

	oddnum := [5]int{1, 3, 5, 7, 9}

	for _, value := range oddnum {
		fmt.Println(value)
	}

	for i, value := range oddnum {
		fmt.Println(i, value)
	} // i will be the index for the same

	// slicing the array
	numSlice := []int{5, 4, 3, 2, 1}
	sliced := numSlice[0:]
	sliced1 := numSlice[:5]
	sliced2 := numSlice[3:5] // does not include 5th element, until 5th element
	fmt.Println(sliced)
	fmt.Println(sliced1)
	fmt.Println(sliced2)

	newSlice := make([]int, 5)
	fmt.Println("New empty zeroed array [0 0 0 0 0]")
	fmt.Println(newSlice)
	copy(newSlice, numSlice)
	fmt.Println(newSlice)
	sliceAppend := append(newSlice, 3, 0, 1)
	fmt.Println(sliceAppend)

}

// execute this file using go run arrays.go
