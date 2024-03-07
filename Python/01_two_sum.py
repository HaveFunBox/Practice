def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    i = 0
    j = 1
    found = False

    while not found:
        while i+j < len(nums):
            if target - nums[i] == nums[i+j]:
                found = True
                break
            j += 1
        if found != True:
            i += 1
            j = 1
        
        
    
    return [i, i+j]

numbers = [2,7,11,15]
t = 9
print(twoSum(numbers,t))