# Given an array arr of n integers, where arr[i] represents price of the stock on the ith day. 
# Determine the maximum profit achievable by buying and selling the stock at most once. 




#Brute Force Solution -Time complexity:O(n^2),space complexity:O(1)
class Solution(object):
    def maxProfit(self, prices):
        n=len(prices)
        max_profit=0
        for i in range(n):
            for j in range(i+1,n):
                profit=prices[j]-prices[i]
                max_profit=max(max_profit,profit)
        return max_profit
    






#Optimal Solution -Time complexity: O(n),space complexity:O(1)
class Solution(object):
    def maxProfit(self, prices):
        n=len(prices)
        max_profit=0
        min_price=float('inf')
        for price in prices:
            if price<min_price:
                min_price=price
            else:
                max_profit=max(max_profit,price-min_price)
        return max_profit