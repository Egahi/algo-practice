'''
https://leetcode.com/problems/reverse-words-in-a-string
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])

s = 'the  sky is               blue'
obj = Solution()
print(obj.reverseWords(s))