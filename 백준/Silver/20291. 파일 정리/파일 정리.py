from collections import defaultdict
import sys
input = sys.stdin.readline
dic = defaultdict(int)
for _ in range(int(input())):
    dic[input().strip().split('.')[1]] += 1
dic = list(sorted(dic.items()))
for k, v in dic:
    print(k, v)