s = input()
arr = [-1] * 26
for i in s: arr[ord(i)-97] = s.find(i)
print(*arr)