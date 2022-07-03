

class Solution():
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n != 1 and n not in visited:
            visited.add(n)
            n = self.sumSquareDigits(n)
        return n == 1

    def sumSquareDigits(self, n):
        output = 0
        for char in str(n):
            output += int(char)**2
        return output
