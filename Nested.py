def solution(S):
        bracket_dict = {")":"(", "]":"[", "}":"{"}
        stack = []
        for bracket in S:
            if bracket == "(" or bracket == "[" or bracket == "{":
                stack.append(bracket)
            elif bracket == ")" or bracket == "]" or bracket == "}":
                if not stack:
                    return 0
                if stack.pop() == bracket_dict[bracket]:
                    continue
                else:
                    return 0
            else:
                return 0
        if len(stack) > 0:
            return 0
        return 1
