'''
https://leetcode.com/problems/missing-ranges
'''
from typing import List

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        def formatRange(lower, upper):
            if lower == upper:
                return str(lower)
            else:
                return str(lower) + '->' + str(upper)

        nums = [lower - 1] + nums + [upper + 1]
        output = []

        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] > 1:
                output.append(formatRange(nums[i] + 1, nums[i+1] - 1))

        return output

obj = Solution()
nums = [0,1,3,50,75,99]
lower = 0
upper = 99
print(nums)
print(obj.findMissingRanges(nums, lower, upper))