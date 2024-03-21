package main

import "fmt"

func removeDuplicates(nums []int) int {
	j := 0
	unique := make(map[int]int)
	for i := 0; i < len(nums); i++ {
		if unique[nums[i]] == 0 {
			unique[nums[i]] = 1
			nums[j] = nums[i]
			j = j + 1
		}
	}
	return j
}

func main() {
	a := []int{1, 2, 3, 3, 4, 5}
	fmt.Println(removeDuplicates(a))
	fmt.Println(a)
}
