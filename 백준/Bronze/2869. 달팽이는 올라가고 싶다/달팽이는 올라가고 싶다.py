import math
a, b, v = map(float, input().split())
print(math.ceil((v-b)/(a-b)))