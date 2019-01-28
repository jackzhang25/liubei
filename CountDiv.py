def solution(A, B, K):
    # write your code in Python 3.6
    nums = 0
    for i in range(A,B+1):
        if i % K == 0:
            nums += 1
        
    return nums
