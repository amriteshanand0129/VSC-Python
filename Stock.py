class Stock:
    # quantity = 0
    # buyDay = 0
    # sellDay = 0

    def __init__(self, quantity, buyday, sellday):
        self.quantity = quantity
        self.buyDay = buyday
        self.sellDay = sellday


N = int(input())
stockData = []
for i in range(N):
    quantity = int(input())
    buyDay = int(input())
    sellDay = int(input())
    stockData.append(Stock(quantity, buyDay, sellDay))

M = int(input())
stockPrices = [[]]
for i in range(N):
    prices = []
    for j in range(M):
        prices.append(int(input()))
    if prices:
        stockPrices.append(prices)
print(stockPrices)
K = int(input())
realizedProfit = unrealizedProfit = 0
for i in range(N):
    stock = stockData[i]
    if stock.buyDay > K:
        continue
    if stock.sellDay == 0 or stock.sellDay > K:
        unrealizedProfit += (stockPrices[i][K - 1] - stockPrices[i][stock.buyDay - 1]) * stock.quantity
    elif stock.sellDay <= K:
        realizedProfit += (stockPrices[i][stock.sellDay - 1] - stockPrices[i][stock.buyDay - 1]) * stock.quantity
print("Realized Profit: ", realizedProfit)
print("Unrealized Profit: ", unrealizedProfit)
