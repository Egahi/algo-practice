'''
https://leetcode.com/problems/increasing-triplet-subsequence
'''
from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_num = second_num = float('inf')

        for num in nums:
            if num < first_num:
                first_num = num
            elif num < second_num:
                second_num = num
            else:
                return True

        return False

obj = Solution()
nums = [1,2,3,4,5]
nums = [5,4,3,2,1]
nums = [1,2,0,3]
print(obj.increasingTriplet(nums))