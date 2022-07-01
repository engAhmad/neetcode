class Solution:
    def sub_sets(self, nums: list[int]) -> list[list[int]]:
        response = []
        subset = []

        def depth_first_search(i):
            if i >= len(nums):
                response.append(subset.copy())
                return
            # decision to include nums[i]
            subset.append(nums[i])
            depth_first_search(i + 1)
            # decision NOT to include nums[i]
            subset.pop()
            depth_first_search(i + 1)

        depth_first_search(0)
        return response
