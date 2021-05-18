'''
https://leetcode.com/problems/subsets
'''
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr, idx):
            if k == len(curr):
                output.append(curr[:])
                return

            for i in range(idx, n):
                curr.append(nums[i])
                backtrack(curr, i + 1)
                curr.pop()

        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack([], 0)

        return output

nums = [1,2,3]
obj = Solution()
print(obj.subsets(nums))