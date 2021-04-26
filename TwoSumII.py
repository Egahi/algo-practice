'''
https://leetcode.com/problems/3sum/
'''
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1

        while start < end:
            if numbers[start] + numbers[end] == target:
                return [start+1, end+1]
            elif numbers[start] + numbers[end] > target:
                end -= 1
            else:
                start += 1

numbers = [2,7,11,15]
#numbers = [3,5,5,7]
target = 9
obj = Solution()
print(obj.twoSum(numbers, target))