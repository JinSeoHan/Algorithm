h, m = map(int, input().split())
time = int(input())
totalTime = time + m
print((h+totalTime//60)%24, totalTime%60)