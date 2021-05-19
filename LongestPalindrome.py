'''
https://leetcode.com/problems/longest-palindromic-substring
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(s, left, right):
            while 0 <= left and right < n and s[left] == s[right]:
                left -= 1
                right += 1

            return right - left - 1
        
        start = end = 0
        n = len(s)
        for i in range(n):
            length1 = expand(s, i, i)
            length2 = expand(s, i, i + 1)
            length = max(length1, length2)

            if length > (end - start):
                start = i - (length - 1) // 2
                end = i + (length // 2)

        return s[start:end + 1]

s = 'babad'
obj = Solution()
print(obj.longestPalindrome(s))
