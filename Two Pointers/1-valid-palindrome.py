class Solution:
    def isPalindrome(self,s:str) ->bool:
        l,r = 0,len(s)-1

        while l<r:
            while l< r and not self.alphanum(s[l]):
                l+=1
            while l< r and not self.alphanum(s[r]):
                r -=1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
# helper function to ditermin the character is Aa-Zz-09 only
    def alphanum(self,c):
        return (ord('A')<=ord(c)<=ord('Z') or
                ord('a')<=ord(c)<=ord('z') or
                ord('0')<=ord(c)<=ord('9') )
# run the example to test
s = "A man, a plan, a canal: Panama"
d = Solution()
print(d.isPalindrome(s))
# run the example to test 2
c = "race a car"
x= Solution()
print(x.isPalindrome(c))