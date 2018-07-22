def twoSum(nums, target):
    for num in nums:
        target1 = target - num
        for num in nums:
            if num == target1:
                answer = num
    print answer
    print target - answer
list_num = [4, 5, 6, 3]    
twoSum(list_num, 9)
