'''
https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/788/
'''
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def buildTree(left, right):
            nonlocal preorder_idx

            if left > right:
                return

            root_val = preorder[preorder_idx]
            preorder_idx += 1
            root = TreeNode(root_val)
            
            root.left = buildTree(left, inorder_indices[root_val] - 1)
            root.right = buildTree(inorder_indices[root_val] + 1, right)

            return root
        
        preorder_idx = 0
        inorder_indices = {}
        for idx, val in enumerate(inorder):
            inorder_indices[val] = idx

        return buildTree(0, len(preorder) - 1)


preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
obj = Solution()
print(obj.buildTree(preorder, inorder))