import sys
input = sys.stdin.readline

def mul(count):
    if count in dic.keys():
        return dic[count]    
    v = 0
    if count % 2 == 0:
        v = mul(count//2)**2%c
    else:
        v = mul(count//2)*mul(count//2+1)%c
    dic[count] = v

    return v

a, b, c = map(int, input().split())
dic = dict()
dic[1] = a%c
print(mul(b))