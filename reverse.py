class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = 0
        reversed_value = 0 
        if x < 0:
            s = x[0]
        while x > 0:
            reversed_value = reversed_value * 10 + x % 10
            x /= 10
        return s + reversed_value
