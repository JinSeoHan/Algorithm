while(True):
    N = int(input())
    if N == -1: break
    result = []
    strResult = ''
    for i in range(1, N):
        if N % i == 0:
            result.append(i)
            strResult += str(i) + ' + '
    if N == sum(result):
        print(f'{N} = {strResult[:-3]}')
    else:
        print(f'{N} is NOT perfect.')