package main

import "fmt"

func removeElement(nums []int, val int) int {
	valNum := 0
	for i := 0; i < len(nums); i++ {
		if nums[(len(nums)-1)-i] == val {
			nums[(len(nums)-1)-i] = nums[(len(nums)-1)-valNum]
			valNum = valNum + 1
		}
	}
	return len(nums) - valNum
}

func main() {
	a := []int{0, 1, 2, 2, 3, 0, 4, 2}
	v := 2
	fmt.Println(removeElement(a, v))
	fmt.Println(a)
}
