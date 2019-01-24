def solution(A):
    if len(A) == 1 and A[0] != 1:
        return 1
    if len(A) == 1 and A[0]== 1:
        return 2
    # write your code in Python 3.6
    for i in range(1,len(A)):
        for num in A:
            if i == num:
                break
            if i != num and num == A[-1]:
                return i 
    return i + 2
