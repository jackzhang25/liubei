class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits)
        while i > 0:
            if digits[i - 1] == 9:
                digits[i - 1] = 0
                i -= 1
            else:
                digits[i - 1] += 1
                break
        if i == 0:
            digits.insert(0,1)
        #If the list is all 9s
        return digits
