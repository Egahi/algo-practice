'''
https://leetcode.com/problems/generate-parentheses
'''
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(S, left, right):
            if len(S) == 2 * n:
                ans.append(''.join(S))
                return

            if left < n:
                S.append('(')
                backtrack(S, left + 1, right)
                S.pop()

            if right < left:
                S.append(')')
                backtrack(S, left, right + 1)
                S.pop()

        ans = []
        backtrack([], 0, 0)
        return ans

n = 3
obj = Solution()
print(obj.generateParenthesis(n))