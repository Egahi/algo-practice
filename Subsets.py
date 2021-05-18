'''
https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/796/
'''
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(idx, curr):
            if len(curr) == k:
                output.append(curr[:])
                return

            for i in range(idx, n):
                curr.append(nums[i])
                backtrack(i + 1, curr)
                curr.pop()
            
        
        output = []
        n = len(nums)
        path = []

        for k in range(n + 1):
            backtrack(0, [])

        return output

nums = [1,2,3]
obj = Solution()
print(obj.subsets(nums))