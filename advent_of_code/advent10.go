package main

import (
	"fmt"
	"strconv"
)

func main() {

	result := "1113222113"
	for i := 0; i < 50; i++ {
		result = nextInt(result)
	}
	// result := nextInt(input)
	// result2 := nextInt(result)
	fmt.Println(len(result))
	// fmt.Println(result)
	// fmt.Println(result2)
}

func nextInt(current string) string{
	previous := "-1"
	sequence := ""
	result := ""

	if len(current) == 1 {

		return "1" + current
	}

	for i, integer := range(current) {
		if len(sequence) == 0 {
			sequence = sequence + string(integer)
			previous = string(integer)
		} else if previous == string(integer) {
			sequence = sequence + string(integer)
		} else if previous != string(integer) {
			sequence_length := strconv.Itoa(len(sequence))
			result = result + sequence_length + previous
			previous = string(integer)
			sequence = string(integer)
		}
		if i+1 == len(current) {
			sequence_length := strconv.Itoa(len(sequence))
			result = result + sequence_length + previous
			previous = string(integer)
			sequence = ""
		}
		
	}
	
	return result
}