class Solution:
    def stockBuySell(self, arr, n):
        min_price = arr[0]
        max_profit = 0
        for i in range(1,len(arr)):
            curr_price = arr[i]
            profit = curr_price - min_price
            max_profit = max(max_profit,profit)
            if curr_price < min_price:
                min_price = curr_price
        return max_profit