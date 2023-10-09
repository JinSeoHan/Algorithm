def solution(numbers):
    
    length = len(numbers)
    stack = []
    result = [-1] * length
    for i,num in enumerate(numbers):
        if len(stack) == 0 or stack[-1][1] >= num:
            stack.append((i,num))
            continue
        
        while stack and stack[-1][1] < num:
            j, _  = stack.pop()
            result[j] = num
        stack.append((i, num))
            
    return result