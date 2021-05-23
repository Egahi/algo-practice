'''
https://leetcode.com/explore/interview/card/microsoft/30/array-and-strings/173/
'''
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for idx, element in enumerate(nums):
            complement = target - element
            if complement in map:
                return [idx, map[complement]]

            map[element] = idx

        return

nums = [2,7,11,15]
target = 9
obj = Solution()
print(obj.twoSum(nums, target))