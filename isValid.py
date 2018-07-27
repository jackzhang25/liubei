    def isValid(s):
        bracket_dict = {")":"(", "]":"[", "}":"{"}
        stack = []
        for bracket in s:
            if bracket == "(" or bracket == "[" or bracket == "{":
                stack.append(bracket)
            elif bracket == ")" or bracket == "]" or bracket == "}":
                if not stack:
                    return False
                if stack.pop() == bracket_dict[bracket]:
                    continue
                else:
                    return False
            else:
                return False
        if len(stack) > 0:
            return False
        return True
