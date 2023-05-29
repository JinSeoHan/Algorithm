import sys
input = sys.stdin.readline

def recursion(s : str, startIdx : int, endIdx : int, count : int):
    if startIdx >= endIdx:
        return (1, count)
    if s[startIdx] == s[endIdx]:
        return recursion(s, startIdx+1, endIdx-1, count+1)
    else:
        return (0, count)

def isPalindrome(s : str) -> tuple:
    return recursion(s, 0, len(s)-1, 1)

for _ in range(int(input())):
    s = input().rstrip()
    result, count = isPalindrome(s)
    print(result, count)