package main

import (
	"fmt"
	"net/http"
)

type Hello struct{}
func (h Hello) ServeHTTP(
	w http.ResponseWriter,
	r *http.Request) {
	fmt.Fprint(w, "Hello WebService...!!!")
}

func main(){
	var h Hello
	http.ListenAndServe(":9000",h)
}
