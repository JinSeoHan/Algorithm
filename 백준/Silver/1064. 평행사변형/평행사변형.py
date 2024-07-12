ax, ay, bx, by, cx, cy = map(int, input().split())

if (ax-cx)*(ay-by) == (ax-bx)*(ay-cy):
    print(-1.0)
    exit(0)

abLength = ((ax-bx)**2 + (ay-by)**2)**0.5
acLength = ((ax-cx)**2 + (ay-cy)**2)**0.5
bcLength = ((bx-cx)**2 + (by-cy)**2)**0.5

length = [abLength+acLength, abLength+bcLength, bcLength+acLength]
result = max(length) - min(length)
print(result*2)