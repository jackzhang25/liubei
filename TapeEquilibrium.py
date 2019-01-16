def solution(A):
    
    # write your code in Python 3.6
    lowest = 100001
    current = 0
    val = 0
    subed_val = 0
    for num in A:
        subed_val += num
    while current < len(A) - 1:
        val += A[current]
        subed_val -= A[current]
        value = val - subed_val
        if value < 0:
            value *= -1
        if value < lowest:
            lowest = value
        current += 1 
    return lowest
