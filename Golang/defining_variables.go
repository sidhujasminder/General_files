package main

import "fmt"

func main() {
	var a = 5 // need not tell that type of a is int
	var b int8 = 12
	var c int16 = 15
	var d int32 = 20

	var floatvar1 float32 = 5.1234
	var floatvar2 = 5.233243523 // Need not define float64 type as Go will understand automatically

	const pi = 3.1415

	var (
		x = 2.0
		y = 6.0
	)

	var1, var2 := 4, 5 // defining multiple variables

	fmt.Println(a)
	fmt.Println(b)
	fmt.Println(c)
	fmt.Println(d)
	fmt.Println(floatvar1)
	fmt.Println(floatvar2)
	fmt.Println(pi)
	fmt.Println(x, y)
	fmt.Println(var1, var2)

	// Checking some arithmetic operations in go

	fmt.Println("sum", x+y)
	fmt.Println("difference", x-y)
	fmt.Println("multiply", x*y)
	fmt.Println("division", x/y)
	fmt.Println("modulus", var1%var2)
	// fmt.Println("modulus", x%y)

	// defining Boolean
	isbool := true
	var isbool1 bool = false // We can or cannot write the bool specifier
	var isbool2 = false

	fmt.Println(isbool && isbool1)
	fmt.Println(isbool || isbool1 || isbool2)
	fmt.Println(!isbool)

}
