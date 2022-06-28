class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # using set to add the numbers without duplicate
        # return true if the number exist in the set
        # otherwise return false
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False


# run the example to test
nums = [1, 2, 3, 1]
d = Solution()
print(d.containsDuplicate(nums))
