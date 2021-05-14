'''
https://leetcode.com/explore/interview/card/top-interview-questions-medium/111/dynamic-programming/807/
'''
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = ['U']*(len(nums) - 1)
        memo.append('G')

        for i in range(len(nums) - 2, -1, -1):
            furthestJump = min(i + nums[i], len(nums) - 1)
            for j in range(i + 1, furthestJump + 1):
                if memo[j] == 'G':
                    memo[i] = 'G'
                    break

        return  memo[0] == 'G'

nums = [2,3,1,1,4]
nums = [1,2]
nums = [0,2,3]
obj = Solution()
print(obj.canJump(nums))