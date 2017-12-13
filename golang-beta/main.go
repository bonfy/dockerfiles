package main

import (
	"fmt"
	"os"
)

func main() {
	if len(os.Args) < 2 {
		fmt.Printf("usage: %s params\n", os.Args[0])
	}

	fmt.Println("Your input:", os.Args[1:])
}
