package main

import "fmt"

func main() {
	var name string = "Jasminderpal Singh Sidhu"
	fmt.Println(name + " is from Punjab")

	fmt.Println(len(name))

	// Print format's using fmt.Printf()
	const pi float64 = 3.142345322
	isbool := true
	x := 5
	fmt.Printf("%f is value of my pi.\n", pi)
	fmt.Printf("%.3f is value of my pi, till precision 3.\n", pi) // precision till 3 points
	fmt.Printf("%T \n", pi)
	fmt.Printf("%T \n", name)
	fmt.Printf("%t \n", isbool)
	fmt.Printf("%d \n", x)
	fmt.Printf("%b \n", x)
	fmt.Printf("%c \n", 33) // print the ascii codes for this value
	fmt.Printf("%x \n", 14) // print hex code for the value
	fmt.Printf("%e \n", pi) // scientific print
}

// execute this file using go run format_print_and_string.go
