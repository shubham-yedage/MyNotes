// DBConnector1
package main

import (
	"database/sql"
	"fmt"

	_ "github.com/go-sql-driver/mysql"
)

func main() {
	fmt.Println("Hello World!")

	db, err := sql.Open("mysql", "root:shubham5252@/my_database")
	checkErr(err)

	rows, err := db.Query("select * from person")
	checkErr(err)

	for rows.Next() {
		var id int
		var name string

		err = rows.Scan(&id, &name)
		checkErr(err)

		fmt.Println(id)
		fmt.Println(name)
		//fmt.Println(id + "----" + name)
	}
}
func checkErr(err error) {
	if err != nil {
		panic(err)
	}
}
