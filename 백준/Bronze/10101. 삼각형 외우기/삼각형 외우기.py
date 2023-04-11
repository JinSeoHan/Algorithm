import sys
ag = []
for _ in range(3):
    ag.append(int(sys.stdin.readline()))
    

if ag.count(ag[0]) == 3:
    print('Equilateral')
elif sum(ag) == 180:
    if ag[0] != ag[1] != ag[2] and ag[0] != ag[2]:
        print('Scalene')
    else:
        print('Isosceles')
else:
    print('Error')