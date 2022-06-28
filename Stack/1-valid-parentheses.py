class Solution:
    def isValid(self, s: str) -> bool:
        # dictionary type that supports key-value pairs.
        map = {")": "(", "]": "[", "}": "{"}
        # set for storing the c value
        stack = []
        for c in s:
            # add the c value if not exist in the map dictionary
            if c not in map:
                stack.append(c)
                continue
            # return false if the list empty or last added value not
            # equal the value in the map
            if not stack or stack[-1] != map[c]:
                return False
            # remove the last added value once we have match pattern
            stack.pop()
        # return true the list is empty or false is not
        return not stack


# Test the Solution
s = "()"
d = Solution()
print(d.isValid(s))
