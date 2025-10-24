from typing import List

# Мое решение
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_pr = prices[0]
        max_pr = prices[0]
        all_benefits = []

        for i in range(len(prices)):
            if prices[i] < min_pr:
                min_pr = prices[i]
                max_pr = prices[i]
            if prices[i] > max_pr:
                max_pr = prices[i]
                ben = max_pr - min_pr
                all_benefits.append(ben)

        if len(all_benefits) > 0:
            return max(all_benefits)
        else:
            return 0

sol = Solution()
print(sol.maxProfit(prices = [7,1,5,3,6,4]))
print(sol.maxProfit(prices = [2,4,1]))
print(sol.maxProfit(prices = [7,6,4,3,1]))

# Решение от ChatGPT

class GPTSolution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_benefit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif (price - min_price) > max_benefit:
                max_benefit = price - min_price
        return max_benefit


solgpt = GPTSolution()
print(solgpt.maxProfit(prices = [7,1,5,3,6,4]))
print(solgpt.maxProfit(prices = [2,4,1]))
print(solgpt.maxProfit(prices = [7,6,4,3,1]))

