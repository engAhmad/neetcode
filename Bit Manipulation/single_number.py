

class Solution:

    # Runtime 219 ms o(n)
    # Memory 16.7 MB o(1)
    def singleNumberBit(self, nums: list[int]) -> int:
        respons = 0
        for n in nums:
            respons = n ^ respons
        return respons

    # Runtime 6895 ms O(n2)
    # Memory 16.8 MB O(1)
    def singleNumber(self, nums: list[int]) -> int:
        for n in nums:
            if nums.count(n) == 1:
                return n
