def fac(num : int) -> int:
    if num <= 1:
        return 1
    return num * fac(num-1)
print(fac(int(input())))