'''
https://leetcode.com/problems/permutations
'''
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first):
            if first == n:
                output.append(nums[:])

            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]

        output = []
        n = len(nums)
        backtrack(0)
        return output

nums = [1,2,3]
obj = Solution()
print(obj.permute(nums))