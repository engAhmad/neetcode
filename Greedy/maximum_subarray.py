class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        response = nums[0]
        total = 0
        for n in nums:
            total += n
            response = max(response, total)
            if total < 0:
                total = 0
        return response
