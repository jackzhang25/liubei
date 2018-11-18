class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        """
        if n == 1:
            return "1"
        if n == 0:
            return "0"
        current = 2
        previous_value = "11"
        return_value = ""
        amount = 0
        run_throughs = 0
        i = 0
        while current <= n:
            if i == len(previous_value) - 1:
                return_value += "1" + previous_value[i]
                previous_value = return_value
                return_value = ""
                i = 0
                current += 1
                continue
            elif previous_value[i] == previous_value[i + 1]:
                while previous_value[i] == previous_value[i + 1] and i > len(previous_value):
                    if run_throughs == 0:
                        i += 2
                        amount += 2
                    else:
                        i += 1
                        amount += 1
                return_value += str(amount) + previous_value[i]
                continue
            else:
                return_value += "1" + previous_value[i]
                continue
        return return_value
        """
        if n == 1:
            return "1"
        num = "1"
        return_value = ""
        def generate_next(num):
            number_temp = -1
            count = 1
            result = ""
            for i in range(len(num)):
                if i < len(num) - 1 and num[i] == num[ i + 1]:
                    count += 1
                if (i < len(num) - 1 and num[i] != num[i + 1]) or i == len(num) - 1:
                    result += str(count)
                    result += str(num[i])
                    count = 1
            return result
        
        for n in range(n - 1):
            num = generate_next(num)
        return_value += num
        
        return return_value            
                
