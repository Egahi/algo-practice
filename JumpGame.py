'''
https://leetcode.com/explore/interview/card/top-interview-questions-medium/111/dynamic-programming/807/
'''
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def canJumpFromPosition(position, nums):
            if position == len(nums) - 1:
                return True

            furthestJump = min(position + nums[position], len(nums) - 1)
            
            for nextPosition in range(position + 1, furthestJump + 1):
                if canJumpFromPosition(nextPosition, nums):
                    return True

            return False
            
        return  canJumpFromPosition(0, nums)

nums = [2,3,1,1,4]
obj = Solution()
print(obj.canJump(nums))