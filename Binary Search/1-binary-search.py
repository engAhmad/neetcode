class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # init left and right pointers
        left, right = 0, len(nums) - 1
        while left <= right:
            # calculate the middle index
            # (l + r) // 2 can lead to overflow
            middle = left + ((right - left) // 2)
            # decrement middle pointer && asign it to the right
            # if the value grater than the target
            if nums[middle] > target:
                right = middle - 1
            # increment middle pointer && asign it to the left
            # if the value less than the target
            elif nums[middle] < target:
                left = middle + 1
            # return founded target
            else:
                return middle
        # otherwise return -1
        return -1


# run the example to test
nums = [-1,0,3,5,9,12]
target = 9
d = Solution()
print(d.search(nums, target))
