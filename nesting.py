def solution(S):

        stack = []
        for bracket in S:
            if bracket == "(":
                stack.append(bracket)
            elif bracket == ")":
                if not stack:
                    return 0
                if stack.pop() == "(":
                    continue
                else:
                    return 0
            else:
                return 0
        if len(stack) > 0:
            return 0
        return 1
