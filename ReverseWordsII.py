'''
https://leetcode.com/problems/reverse-words-in-a-string-ii
'''
from typing import List

class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverseWord(s, start, end):
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1

        s.reverse()
        start = 0
        for i in range(len(s)):
            if s[i] == ' ':
                reverseWord(s, start, i - 1)
                start = i + 1

        reverseWord(s, start, len(s) - 1)


s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
obj = Solution()
obj.reverseWords(s)
        