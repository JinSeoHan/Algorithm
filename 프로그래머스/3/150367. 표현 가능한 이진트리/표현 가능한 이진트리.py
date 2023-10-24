import math
import sys
sys.setrecursionlimit(10**9)
def solution(numbers):
    result = []
    for number in numbers:
        b = bin(number)
        b = list(b[2:])
        n = 1
        while 2**n-1 < len(b):
            n += 1
        for i in range(len(b)-1, 2**n-2):
            b = ['0'] + b

        if valid(b, 1):
            result.append(1)
        else:
            result.append(0)
    return result
    
def valid(l, parent):
    mid = len(l)//2
    if parent == '0' and l[mid] == '1': return False
    if l[mid] == '0':
        parent = '0'
    
    if len(l) == 1:
        return True
    left = valid(l[:mid], parent)
    right = valid(l[mid+1:], parent)
    
    return left and right