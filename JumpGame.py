'''
https://leetcode.com/explore/interview/card/top-interview-questions-medium/111/dynamic-programming/807/
'''
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastPos = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= lastPos:
                lastPos = i

        return  lastPos == 0

nums = [2,3,1,1,4]
#nums = [1,2]
#nums = [0,2,3]
obj = Solution()
print(obj.canJump(nums))