import sys
input = sys.stdin.readline

cash = int(input())
stockPrices = list(map(int, input().split()))

def getBNP(cash, stockPrices):
    # 주식수
    stockCnt = 0
    for stockPrice in stockPrices:
        if stockPrice <= cash:
            stockCnt += cash // stockPrice # 구입한 주식개수
            cash -= (cash // stockPrice) * stockPrice # 잔돈저장
    return cash + stockCnt*stockPrices[-1]

def getTiming(cash, stockprices):
    # 주식수
    stockCnt = 0
    upCnt = 0
    downCnt = 0
    for i in range(1, len(stockprices)):#0,1,2,3
        # 매수타이밍 체크
        if stockprices[i-1] > stockprices[i]:
            downCnt += 1
            upCnt = 0
            if downCnt >= 3:
                stockCnt += cash // stockprices[i]
                cash %= stockprices[i]
        # 매도타이밍 체크
        if stockprices[i-1] < stockprices[i]:
            upCnt += 1
            downCnt = 0
            if upCnt >= 3:
                cash += stockprices[i] * stockCnt
                stockCnt = 0
        # 값이 같이면 초기화
        if stockPrices[i-1] == stockprices[i]:
            upCnt, downCnt = 0, 0
    return cash + stockCnt * stockprices[-1]


bnp = getBNP(cash, stockPrices)
timing = getTiming(cash, stockPrices)

if bnp > timing:
    print("BNP")
elif bnp < timing:
    print("TIMING")
else:
    print("SAMESAME")
