def singleNumber(nums):
    return_value = 0
    for num in nums:
        return_value = return_value ^ num
    return return_value
