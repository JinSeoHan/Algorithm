n, k = map(int, input().split())
l = list(map(int, input().split()))
endPoint = sum(l)

# course1
course1 = [[0, 1]]
for i, v in enumerate(l):
    course1.append([course1[-1][0]+v, i+1])
# cousre2
course2 = [[0,course1[-1][1]]]
for i, v in enumerate(reversed(l)):
    course2.append([course2[-1][0]+v, len(l)-i])

if k <= endPoint:
    for point, num in course1:
        if k < point:
            print(num)
            break
else:
    k -= endPoint
    for point, num in course2:
        if k < point:
            print(num)
            break