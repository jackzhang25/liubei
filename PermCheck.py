def solution(A):
    if len(A) == 1 and A[0] == 1:
        return 1
    if len(A) == 1: return 0

    for num in range(1, len(A)+1):
        for item in A:
            if num == item:
                break
            elif A[-1] == item and num != item:
                return 0
    return 1
