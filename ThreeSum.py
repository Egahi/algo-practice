'''
https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/776/
'''
from typing import List
from collections import Counter

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i != 0 and nums[i] == nums[i-1]:
                continue
            
            low, high= i + 1, len(nums) - 1

            while low < high:
                if nums[i] + nums[low] + nums[high] < 0:
                    low += 1
                elif nums[i] + nums[low] + nums[high] > 0:
                    high -= 1
                else:
                    output.append([nums[i], nums[low], nums[high]])
                    low += 1
                    high -= 1

                    while low < high and nums[low] == nums[low-1]:
                        low += 1

        return output
        
nums = [-12,12,-5,-4,-12,11,9,-11,13,1,12,-1,8,1,-9,-11,-13,-4,10,-9,-6,-11,1,-15,-3,4,0,-15,3,6,-4,7,3,-2,10,-2,-6,4,2,-7,12,-1,7,6,7,6,2,10,-13,-3,8,-12,2,-5,-12,6,6,-5,6,-5,-14,9,9,-4,-8,4,2,-7,-15,-11,-7,12,-4,8,-5,-12,-1,12,5,1,-5,-1,5,12,9,0,3,0,3,-14,2,-4,2,-4,0,1,7,-13,9,-1,13,-12,-11,-6,11,-1,-10,-5,-3,10,3,7,-6,-15,-4,10,1,14,-12]

#nums = [-1,0,1,2,-1,-4]
obj = Solution()
print(obj.threeSum(nums))
        