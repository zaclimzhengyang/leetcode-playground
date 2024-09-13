class Solution(object):
    def maxProfit(self, prices):
        max_profit: int = 0
        curr_price: int = prices[0]
        for i in range(len(prices)):
            curr_price: int = min(curr_price, prices[i])
            max_profit = max(max_profit, prices[i] - curr_price)
        return max_profit


my_solution = Solution()
result = my_solution.maxProfit([7, 1, 5, 3, 6, 4])
print(result)