class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l,r=0,1 # Left buy , Right sell
        maxP = 0 # initialize maxProfit as 0
        # loop throw the prices list 
        while r < len(prices):
            # is profitable ?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                # update the maximum profit 
                maxP = max(maxP,profit)
            else:
                # not profitable we update left pointer with the right
                l = r
            # update the right pointer to continue the loop 
            r += 1
        return maxP

# Test the Solution
prices = [7,1,5,3,6,4]
d = Solution()
print(d.maxProfit(prices))