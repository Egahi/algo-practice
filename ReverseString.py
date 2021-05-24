'''
https://leetcode.com/problems/reverse-string
'''
from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        #s.reverse()

        for i in range(len(s) // 2):
            s[i], s[~i] = s[~i], s[i]
        

s = ["h","e","l","l","o"]
obj = Solution()
obj.reverseString(s)