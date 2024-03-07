def summaryRanges(nums):
    """
    :type nums: List[int]
    :rtype: List[str]
    """
    if len(nums) < 2:
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        return nums
    ranges = []
    start = 0
    for i in range(1,len(nums)):
        if nums[i] != nums[i-1] + 1:
            if i - start == 1:
                ranges.append(str(nums[start]))
            else:
                ranges.append(str(nums[start])+"->"+str(nums[i-1]))
            start = i    
    if start == len(nums) - 1:
        ranges.append(str(nums[start]))
    else:
        ranges.append(str(nums[start])+"->"+str(nums[len(nums)-1]))
    return ranges

def summaryRangesFast(nums):
    ranges = []
    i = 0
    while i < len(nums):
        start = nums[i]
        while i < len(nums) -1 and nums[i+1] - nums[i] == 1:
            i += 1
        if start == nums[i]:
            ranges.append(str(start))
        else:
            ranges.append(str(start)+"->"+str(nums[i]))
        i += 1
    return ranges
        



test = [0,2,3,4,6,8,9]
test2 = []
print(summaryRangesFast(test2))

