package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

func main() {

	input, err := ioutil.ReadFile("advent5_input.txt")
	if err != nil {
		fmt.Println("aww shit")
	}
	naughty_nice_list := strings.Split(string(input), "\n")

	vowels := "aeiou"
	naughty_words := []string{"ab", "cd", "pq", "xy"}

	//line := naughty_nice_list[0]
	// line = "dvszwmarrgswjxmb"
	
	num_nice := 0

	for _, line := range naughty_nice_list {
		last_character := rune(-1)
		num_vowels := 0
		contains_consecutive := false
		contains_naughty_word := false
		for _, letter := range line {	
			if strings.ContainsAny(string(letter), vowels) {
				num_vowels++
			}
			if letter == last_character {
				contains_consecutive = true
			}
			if contains(string(last_character) + string(letter), naughty_words) {
				contains_naughty_word = true
			}
			last_character = letter
		}
		if num_vowels >= 3 && contains_consecutive && !contains_naughty_word {
			num_nice++
		}
	}
	fmt.Println(num_nice)
}

func contains (somestring string, stringList []string) bool {
	for _, s := range stringList {
		if somestring == s {
			return true
		}
	}
	return false
}