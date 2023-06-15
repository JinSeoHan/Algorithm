count1 = 0
def fib(n):
    global count1
    if n == 1 or n == 2:
        count1 += 1
        return 1
    else:
        return fib(n-1) + fib(n-2);

n = int(input())
fib(n)
print(count1, n-2)