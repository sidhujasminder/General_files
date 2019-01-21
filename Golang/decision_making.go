package main

import "fmt"

func main() {

	age := 31
	if age > 18 {
		fmt.Println("You can Vote")
	} else {
		fmt.Println("No you cant vote")
	}

	switch age {
	case 18:
		fmt.Println("Okay ready to vote")
	case 20:
		{
			for i := 1; i < age; i++ {
				fmt.Println("Print ", i)
			}
		}
	default:
		fmt.Println("No Age in switch")
	}

}

// execute this file using go run decision_making.go
