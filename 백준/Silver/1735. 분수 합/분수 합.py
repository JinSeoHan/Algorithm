import sys
input = sys.stdin.readline

def GreatestCommonDivisor(a : int, b : int) -> int:
    big = 0
    small = 0
    remainder = 0

    if a > b:
        big = a
        small = b
    else:
        big = b
        small = a
    
    remainder = big % small

    if remainder == 0:
        return small
    
    return GreatestCommonDivisor(small, remainder)

n1, m1 = map(int, input().split())
n2, m2 = map(int, input().split())
n, m = (n1*m2+n2*m1), (m1*m2)
gcd = GreatestCommonDivisor(n, m)
print(n//gcd, m//gcd)
# 12 38

# 2 6 19
# 유클리드 호제법에 따르면 두 수는 최대 공약수 * 서로소의 곱 페어 관계를 가짐
# ==> 약분을 할 때 최대공약수로 나눠주면 기약분수를 구할 수 있을 것 같음

# 서로소는 어떻게 알 수 있을까? -> 분자/최대공약수 and 분모/최대공약수