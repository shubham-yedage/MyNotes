// ForExample
package main

import (
	"fmt"
)

func main() {
	fmt.Println("Hello World!")

	s := []string{"a", "b", "c", "d", "e", "f"}
	fmt.Println(s)

	l := s[2:5]
	fmt.Println(l)

	k := make([]string, 4)
	fmt.Println(len(k))

	m := []string{}
	fmt.Println(len(m))

	ma := make(map[string]int)

	ma["a1"] = 1
	ma["a2"] = 2

	e, f := ma["a1"]
	fmt.Println(e, f)
	delete(ma, "a2")
	d, c := ma["a2"]
	fmt.Println(d, c)
}
