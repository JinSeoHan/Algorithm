import sys
input = sys.stdin.readline
n = int(input())

sArr = set()

count = 0
for i in range(n):
    s = input()
    if s == "ENTER\n":
        for j in range(i+1, n):
            s = input()
            if s != "ENTER\n":
                sArr.add(s)
            else:
                count += len(sArr)
                sArr.clear()
        break;
count += len(sArr)
print(count)