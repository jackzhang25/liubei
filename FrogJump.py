def solution(X, Y, D):
    if X >= Y:
        return 0 
    # write your code in Python 3.6
    distance = Y - X
    distance /= D
    if distance == int(distance):
        return int(distance)
    return int(distance) + 1  
