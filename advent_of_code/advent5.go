package main

import (
	"fmt"
	"strings"
	"io/ioutil"
)


func main() {
	naughty_nice_input, err := ioutil.ReadFile("advent5_input.txt")
	if err != nil {
		fmt.Println("Damnit-1")
	}
	naughty_nice_list := strings.Split(string(naughty_nice_input), "\n")
	vowels := "aeiou"
	banned := ["ab", "cd", "pq", "xy"]

	first_item := naughty_nice_list[0]
	num_vowels := 0
	has_consecutive := false
	previous_letter := rune(-1)

	for _, letter := range first_item {
		if strings.ContainsAny(string(letter), vowels) {
			num_vowels++
		}
		if previous_letter != rune(-1) {
			consecutive := previous_letter + letter
			if consecutive[0] == consecutive[1] {
				has_consecutive = true
			}
			else {
				for _, ban := range banned {
					
				}
			}

		}
		previous_letter = letter
	}
	fmt.Println(num_vowels)
	fmt.Println(has_consecutive)
	
	// if strings.Contains(naughty_nice_list[0], "a") {
	// 	num_vowels++
	// }  
	// if strings.Contains(naughty_nice_list[0], "e") {
	// 	num_vowels++
	// }  
	// if strings.Contains(naughty_nice_list[0], "i") {
	// 	num_vowels++
	// }  
	// if strings.Contains(naughty_nice_list[0], "o") {
	// 	num_vowels++
	// }  
	// if strings.Contains(naughty_nice_list[0], "u") {
	// 	num_vowels++
	// }

	// num_other := 0
	// if strings.ContainsAny(naughty_nice_list[0], vowels) {
	// 	for _, vowel := range vowels {
	// 		fmt.Println(vowel)
	// 	}
	// }
	// fmt.Println(num_other)

	// fmt.Println(naughty_nice_list[0])
	// fmt.Println(num_vowels)
}