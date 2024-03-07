/*
 * Some of the worst code I have ever written
 * and it doesn't even work...
 */

package main

import (
	"fmt"
	"math"
)

// Definition for singly-linked list.
// type ListNode struct {
// 	Val  int
// 	Next *ListNode
// }

func makeLinkedList(val []int) *ListNode {
	if len(val) == 1 {
		return newListNode(val[0])
	}
	node := newListNode(val[0])
	node.Next = makeLinkedList(val[1:])
	return node
}

func newListNode(val int) *ListNode {
	new := ListNode{Val: val}
	return &new
}

func intToListNode(total float64) *ListNode {
	// fmt.Println(total)
	if total < 10 {
		// fmt.Printf("final: %v\n", int(total))
		return newListNode(int(total))
	}
	// fmt.Println(int(math.Mod(total, 10)))
	final := newListNode(int(math.Mod(total, 10)))
	// Shaves the lowest digit off the integer
	final.Next = intToListNode(math.Floor(total / 10))
	return final
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	total := 0.0
	for i := 0.0; l1 != nil || l2 != nil; i++ {
		fmt.Printf("i: %v\n", i)
		if l1 != nil {
			fmt.Printf("l1 + %v\n", math.Pow(10, i)*float64(l1.Val))
			total = total + math.Pow(10, i)*float64(l1.Val)
			l1 = l1.Next
		}
		if l2 != nil {
			// fmt.Printf("l2 + %v\n", math.Pow(10, i)*float64(l2.Val))
			total = total + math.Pow(10, i)*float64(l2.Val)
			l2 = l2.Next
		}
		// fmt.Printf("Total: %v\n", total)
	}
	return intToListNode(total)
}

func main() {
	test1 := makeLinkedList([]int{1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1})
	test2 := makeLinkedList([]int{5, 6, 4})
	fmt.Println(addTwoNumbers(test1, test2))
}
