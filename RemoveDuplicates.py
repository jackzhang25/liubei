
    def removeDuplicates(self, nums):
        if len(nums) < 2:
            return len(nums)
        i = 0
        current = 0        
        while i < len(nums) - 1:
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    continue        
                else:
                    current += 1            
                    nums[current] = nums[j]
                    break 
            i = j
        return current + 1 
