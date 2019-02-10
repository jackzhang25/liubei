def solution(A, B):
    surviving = 0
    stack = []
     
    for idx in range(len(A)):
        if B[idx] == 0:
            while len(stack) != 0:
                if stack[-1] > A[idx]:
                    break
                else:
                    stack.pop()
                         
            else:
                surviving += 1
        else:
            stack.append(A[idx])
             
    surviving += len(stack)
     
    return surviving
