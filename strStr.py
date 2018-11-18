class Solution(object):
    def strStr(self, haystack, needle):
        if len(needle) == 0:
            return 0
        needle_len = len(needle)
        return_index = -1
        x = 0
        for i in range((len(haystack) - needle_len) + 1):
            for j in range(i, needle_len + i):
                if j == (needle_len + i) - 1 and haystack[j] == needle[x]:
                    return i
                if haystack[j] == needle[x]:
                    x += 1
                    continue
                else:
                    break
            x = 0
        return return_index
