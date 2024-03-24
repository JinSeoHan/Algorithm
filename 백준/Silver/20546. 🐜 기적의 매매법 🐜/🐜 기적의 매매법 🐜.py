money = int(input())
stocks = list(map(int, input().split()))

bnp = 0 # bnp 주식개수
timing = 0 # timing 주식개수


# bnp
bnp_money = money
bnp_result = 0
for stock in stocks:
    if stock <= bnp_money:
        bnp += (bnp_money // stock)
        bnp_money -= (bnp_money // stock) * stock
        # print(bnp, bnp_money)

bnp_result = (stocks[13] * bnp) + bnp_money

down_count = 0 # 연속으로 내려간 날
up_count = 0 # 연속으로 올라간날 
before_stock = 0 # 현재 stock과 비교할 그 전날 stock
now_stock = 0 # 현재 stock


# timing
timing_money = money
timing_result = 0
for i in range(1, len(stocks)):
    before_stock = stocks[i-1]
    now_stock = stocks[i]
    # 매수
    if before_stock > now_stock:
        down_count += 1
        up_count = 0
        if down_count >= 3:
            timing += (timing_money // stocks[i])
            # print(timing_money // stocks[i])
            timing_money -= (timing_money // stocks[i]) * stocks[i]

    # 매도
    if before_stock < now_stock:
        up_count += 1
        down_count = 0
        if up_count >= 3:
            timing_money += timing * stocks[i] 
            timing = 0 
    
    # 초기화
    if before_stock == now_stock:
        down_count = 0
        up_count = 0
    # print(now_stock, up_count, down_count, timing, timing_money)

timing_result = (stocks[13] * timing) + timing_money
# print(bnp_result, timing_result)


if bnp_result > timing_result:
    print('BNP')
elif bnp_result < timing_result:
    print('TIMING')
else:
    print('SAMESAME')
