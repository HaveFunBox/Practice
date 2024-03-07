package main

import "fmt"

var pars = map[byte]byte{
	'(': ')',
	'[': ']',
	'{': '}',
}

// func sameBracket(open, close byte) bool {
// 	// fmt.Println("open: ", open, "close: ", close)
// 	if (open == '(' && close == ')') || (open == '[' && close == ']') || (open == '{' && close == '}') {
// 		// fmt.Println(true)
// 		return true
// 	} else {
// 		return false
// 	}
// }

func isValid(s string) bool {
	stack := make([]byte, 0)
	for i := 0; i < len(s); i++ {
		// fmt.Println(stack)
		if s[i] == '(' || s[i] == '{' || s[i] == '[' {
			stack = append(stack, s[i])
		} else {
			if len(stack) == 0 || s[i] != pars[stack[len(stack)-1]] {
				return false
			}
			stack = stack[:len(stack)-1]
		}
	}
	return len(stack) == 0
}

func main() {
	test := "[]{}()"
	fmt.Println(isValid(test))
}
