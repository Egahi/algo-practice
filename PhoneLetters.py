'''
https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/793/
'''
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtrack(idx, path):
            if len(path) == len(digits):
                output.append(''.join(path))
                return 

            letters = digit_letters[digits[idx]]

            for letter in letters:
                path.append(letter)
                backtrack(idx + 1, path)

                path.pop()

        output = []
        backtrack(0, [])
        return output

digits = '23'
obj = Solution()
print(obj.letterCombinations(digits))