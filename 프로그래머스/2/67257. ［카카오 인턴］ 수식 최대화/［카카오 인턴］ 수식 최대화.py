from itertools import permutations
import re
def getResult(nums, opers, operations):
    i = 0
    while i < len(opers):
        if opers[i] == operations:
            #해당 연산 수행
            value = eval(nums[i] + opers[i] + nums[i+1])
            del nums[i+1]
            del nums[i]
            del opers[i]
            nums.insert(i, str(value))
            continue
        i+= 1
    return nums, opers
def solution(expression):
    nums = re.split('[*+-]', expression) #피연산자 추출
    opers = [v for v in re.split('[^*+-]', expression) if v] #연산자 추출
    os = list(set(opers)) # 피연산자 종류 추출
    
    #모든 경우의 우선순위를 출력
    result = 0
    for order in permutations(os, len(os)):
        newNums = nums.copy()
        newOpers = opers.copy()
        for operation in order:
            newNums, newOpers = getResult(newNums, newOpers, operation)
        result = max(result, abs(int(newNums[0])))
        
    return result