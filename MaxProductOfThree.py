def solution(A): # write your code in Python 3.6 
    neg = 0
    pos = 0
    removed_0 = False
    return_val = 0
    for num in A: 
        if num < 0: 
            neg += 1
        elif num > 0: 
            pos += 1
        elif num == 0:
            A.remove(num)
            removed_0 = True
    A.sort()
    if pos == 0:
        return_val =  A[-1]*A[-2]*A[-3]
    elif pos == 1 or pos == 2:
        return_val =  A[0]*A[1]*A[-1]
    elif neg == 0 or neg == 1:
        return_val =  A[-1]*A[-2]*A[-3]
    else:
        if A[-2]*A[-3] > A[0]*A[1]:
            return_val =  A[-1]*A[-2]*A[-3]
        else:
            return_val =  A[0]*A[1]*A[-1]
            
    if return_val < 0 and removed_0:
        return 0
    return return_val
