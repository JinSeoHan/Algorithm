def solution(s):
    
    result = 10000
    if len(s) == 1:
        return 1
    for size in range(1, len(s)):
        stack = []
        
        sResult = ''
        for i in range(0, len(s) - size + 1, size):
            target = s[i:i+size]
            
            if not stack or stack[-1] == target:
                stack.append(target)
                continue
                
            if len(stack) > 1:
                sResult += str(len(stack)) + stack[0]
            else:
                sResult += stack[0]
            stack = []
            stack.append(target)
        if len(stack) > 1:
            sResult += str(len(stack)) + stack[0]
        else:
            sResult += stack[0]
        
        if len(s) % size != 0:
            sResult += s[len(s) - len(s)%size:]
        
        result = min(result, len(sResult))
        

    return result