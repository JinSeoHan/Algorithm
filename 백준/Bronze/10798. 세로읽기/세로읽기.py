arr = []
for i in range(5):
    arr += [list(input())]
for _ in range(15):
    for j in range(len(arr)):
        if len(arr[j]) > 0: 
            print(arr[j].pop(0), end='')