package main

import (
	"fmt"
	"crypto/md5"
	"encoding/hex"
	"strings"
	//"strconv"
)

func main() {

	const input = "yzbqklnj"
	hasher := md5.New()
	hasher.Write([]byte(input))
	theString := hex.EncodeToString(hasher.Sum(nil))

	found := False
	count := -1
	next := input

	while !found {
		count += 1
		next = count + next
		hasher.Write([]byte(input))
		hash = hex.EncodeToString(hasher.Sum(nil))
		
	}


	//fmt.Printf("%x", strings.Contains(hash, "dd"))
}

	