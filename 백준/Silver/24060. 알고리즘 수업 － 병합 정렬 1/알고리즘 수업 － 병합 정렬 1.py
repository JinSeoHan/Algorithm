import sys
input = sys.stdin.readline

def mergeSort(l : list):
    if len(l) == 1: 
        return l

    mid = (len(l)+1) // 2
    leftL = mergeSort(l[:mid])
    rightL = mergeSort(l[mid:])

    lIdx, rIdx = 0, 0
    mergedL = []
    while lIdx < len(leftL) and rIdx < len(rightL):
        if leftL[lIdx] < rightL[rIdx]:
            mergedL.append(leftL[lIdx])
            storedL.append(leftL[lIdx])
            lIdx += 1
        else:
            mergedL.append(rightL[rIdx])
            storedL.append(rightL[rIdx])
            rIdx += 1
    while lIdx < len(leftL):
        mergedL.append(leftL[lIdx])
        storedL.append(leftL[lIdx])
        lIdx += 1
    while rIdx < len(rightL):
        mergedL.append(rightL[rIdx])
        storedL.append(rightL[rIdx])
        rIdx += 1
    return mergedL

storedL = []
a, k = map(int, input().split())
l = list(map(int, input().split()))

mergeSort(l)

if len(storedL) < k:
    print(-1)
else:
    print(storedL[k-1])