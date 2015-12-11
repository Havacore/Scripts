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

	fmt.Printf("%x", strings.Contains(theString, "9391"))


	//fmt.Printf("%x", strings.Contains(hash, "dd"))
}

	