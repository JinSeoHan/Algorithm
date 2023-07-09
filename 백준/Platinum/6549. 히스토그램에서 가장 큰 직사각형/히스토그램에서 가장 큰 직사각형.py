import sys
input = sys.stdin.readline

def getMaxArea(lIdx, rIdx) -> int:
    if lIdx == rIdx:
        return values[lIdx]
    
    mid = (lIdx+rIdx) // 2
    ma = values[mid]
    lMxArea = getMaxArea(lIdx, mid)
    rMxArea = getMaxArea(mid+1, rIdx)
    ma = max(lMxArea, rMxArea)

    frmL, frmR = mid-1, mid+1
    h = values[mid]
    while lIdx <= frmL or frmR <= rIdx:
        if lIdx <= frmL and frmR <= rIdx:
            if values[frmL] >= values[frmR]:
                frmL -= 1
                h = min(h, values[frmL+1])
            else:
                frmR += 1
                h = min(h, values[frmR-1])
        else:
            if lIdx > frmL:
                frmR += 1
                h = min(h, values[frmR-1])
            else:
                frmL -= 1
                h = min(h, values[frmL+1])
        
        ma = max(ma, (frmR-frmL-1) * h)
    return ma

while (values:=list(map(int, input().split())))[0] != 0:
    
    maxArea = getMaxArea(1, values[0])
    print(maxArea)