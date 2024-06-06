class Solution:
# max profit can be given by taking hte minimum and subtracting that from the max
# it only moves in one direction
# two pointers
# left pointer on day one and right pointer on day two
# this is not the two pointers solution but can do it with two pointers
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        smallest = prices[0]
        for num in prices:
            if num < smallest:
                smallest = num
            max_profit = max(max_profit, num - smallest)
        return max_profit
