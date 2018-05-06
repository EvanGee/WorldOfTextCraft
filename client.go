package main

import (
	"bufio"
	"fmt"
	"io"
	"net"
	"os"
)

func processClient(conn net.Conn) {
	_, err := io.Copy(os.Stdout, conn)
	if err != nil {
		fmt.Println(err)
	}
}

func main() {

	// connect to this socket

	connectionString := "104.131.93.154:1111"
	if len(os.Args) > 1 {
		connectionString = os.Args[1]
	}
	conn, _ := net.Dial("tcp", connectionString)
	reader := bufio.NewReader(os.Stdin)

	go processClient(conn)
	for {
		// read in input from stdin
		text, _ := reader.ReadString('\n')
		// send to socket
		fmt.Fprintf(conn, text)
	}
}
