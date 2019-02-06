package main

import "fmt"

func main() {

	StudentAge := make(map[string]int)
	StudentAge["A"] = 20
	StudentAge["S"] = 21
	StudentAge["D"] = 22
	StudentAge["F"] = 23
	StudentAge["G"] = 24

	fmt.Println(StudentAge)      // map[A:20 S:21 D:22 F:23 G:24]
	fmt.Println(len(StudentAge)) // 5
	fmt.Println(StudentAge["G"]) // 24

	EmpAge := map[string]int{
		"A": 12,
		"B": 14,
	}
	fmt.Println(EmpAge)

	superhero := map[string]map[string]string{
		"superman": map[string]string{
			"realname": "klark",
			"Age":      "21",
			"City":     "metropolis",
		},
		"batman": map[string]string{
			"realname": "bruce",
			"Age":      "21",
			"City":     "gotham",
		},
	}

	// fmt.Println(superhero["batman"])
	temp, s := superhero["batman"] // temp will contain the map and s will contain if the key is present or not true/false
	if s {
		fmt.Println(temp)
	}

}

// execute this file using go run maps.go
