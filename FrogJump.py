def solution(X, Y, D):
    if X >= Y:
        return 0 
    # write your code in Python 3.6
    distance = (Y - X)/D
    int_dis = int(distance)
    if distance == int_dis:
        return int_dis
    return int_dis + 1  
