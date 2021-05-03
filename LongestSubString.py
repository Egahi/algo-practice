'''
https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/779/
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = i = 0
        xters = {}

        for j in range(len(s)):
            if s[j] in xters:
                i = max(xters[s[j]], i)

            ans = max(ans, j - i + 1)
            xters[s[j]] = j + 1

        return ans

s = "abcabcbb"
obj = Solution()
print(obj.lengthOfLongestSubstring(s))