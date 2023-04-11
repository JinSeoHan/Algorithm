x, y, w, h = map(int, input().split())
print(min(h-y, w-x, x, y))