'''
https://leetcode.com/explore/interview/card/microsoft/30/array-and-strings/162/
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_xters = [xter.lower() for xter in s if xter.isalnum()]
        return s_xters == s_xters[::-1]

s = "A man, a plan, a canal: Panama"
obj = Solution()
print(obj.isPalindrome(s))