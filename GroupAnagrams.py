'''
https://leetcode.com/problems/group-anagrams
'''
import collections
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = collections.defaultdict(list)

        for str in strs:
            output[tuple(sorted(str))].append(str)

        return output.values()

strs = ["eat","tea","tan","ate","nat","bat"]
#strs = ["",""]
#strs = ["ddddddddddg","dgggggggggg"]
obj = Solution()
print(obj.groupAnagrams(strs))