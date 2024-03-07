package main

import "fmt"

//  Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

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

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	carry := 0
	head := newListNode(0)
	current := head
	for l1 != nil || l2 != nil || carry != 0 {
		if l1 != nil {
			current.Val = current.Val + l1.Val
			l1 = l1.Next
		}
		if l2 != nil {
			current.Val = current.Val + l2.Val
			l2 = l2.Next
		}
		current.Val = current.Val + carry
		carry = 0
		if current.Val > 9 {
			carry = 1
			current.Val = current.Val - 10
		}
		if l1 != nil || l2 != nil || carry != 0 {
			current.Next = &ListNode{}
			current = current.Next

		}
	}
	return head
}

func main() {
	test1 := makeLinkedList([]int{2, 4, 3})
	test2 := makeLinkedList([]int{5, 6, 4})
	fmt.Println(addTwoNumbers(test1, test2))
}
