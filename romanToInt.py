class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        i = 0
        value_list = []
        return_value = 0
        value_dict = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        for j in range(len(s)): 
            x = value_dict[s[j]]
            value_list.append(x)
        while i < len(value_list):
            if i == len(value_list) - 1:
                return_value += value_list[i]
                break 
            if value_list[i] == value_list[i + 1]:
                return_value += value_list[i] + value_list[i + 1]
                i += 2
                continue
            if value_list[i] > value_list[i + 1]:
                return_value += value_list[i]
                i += 1
                continue
            if value_list[i] < value_list[i + 1]:
                return_value += value_list[i + 1] - value_list[i]
                i += 2
                continue
        return return_value
