package main

import (
	"fmt"
	"math"
)

const s string = "Constant"

func main(){
	fmt.Println(s)

	const c = 20000
	const d = 3e20 / c
	
	fmt.Println(d)

	fmt.Println(int64(d))

	fmt.Println(math.Sin(c))
}
