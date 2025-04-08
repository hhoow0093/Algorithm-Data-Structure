def solve(prices):
    maxprofit = 0
    min_price = float('inf')
    for price in prices:
        # check min price
        if min_price > price:
            min_price = price
        #check profit
        profit  = price - min_price
        #check maxprofit 
        if maxprofit < profit:
            maxprofit = profit
    return maxprofit

def main():
    prices = [7, 1, 5, 3, 6, 4]
    max_profit = solve(prices)
    print(max_profit)  
main()