def fibo(num : int) -> int:
    if num <= 2:
        return 1
    return fibo(num-1) + fibo(num-2)

num = int(input())
if num == 0:
    print(0)
else:
    print(fibo(num))