def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    # if n != 0:
    #     p2 = 0
    #     for i in range(len(nums1)):
    #         if nums1[i] > nums2[p2]:
    #             swap = nums1[i]
    #             nums1[i] = nums2[p2]
    #             nums2[p2] = swap
    #         elif nums1[i] == 0:
    #             nums1[i] = nums2[p2]
    #             p2 += 1
    for _ in range(len(nums1)):
        if m == 0:
            nums1[n-1] = nums2[n-1]
            n -=1
        elif n == 0:
            break
        else:
            if nums1[m-1] >=nums2[n-1]:
                nums1[(m + n)-1] = nums1[m-1]
                nums1[m-1] = 0
                m -= 1
            else:
                nums1[(m + n)-1] = nums2[n-1]
                n -= 1
    print(nums1)

one = [1,2,3,0,0,0]
two = [2,5,6]


merge(one, 3, two, 3)