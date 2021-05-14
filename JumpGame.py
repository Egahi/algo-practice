'''
https://leetcode.com/explore/interview/card/top-interview-questions-medium/111/dynamic-programming/807/
'''
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = ['U']*len(nums)
        def canJumpFromPosition(position, nums):
            if memo[position] != 'U':
                return memo[position] == 'G'

            furthestJump = min(position + nums[position], len(nums) - 1)
            
            for nextPosition in reversed(range(position + 1, furthestJump + 1)):
                if canJumpFromPosition(nextPosition, nums):
                    memo[position] = 'G'
                    return True

            memo[position] = 'B'
            return False

        memo[len(nums) - 1] = 'G'
        return  canJumpFromPosition(0, nums)

nums = [2,3,1,1,4]
obj = Solution()
print(obj.canJump(nums))