def solution(A):
    x = len(A)/2
    num_dict = {}
    for i in range(len(A)):
        num = A[i]
        if num in num_dict:
            num_dict[num] += 1
            
        else:
            num_dict[num] = 1
        
        if num_dict[num] > x:
            return i
    return -1
