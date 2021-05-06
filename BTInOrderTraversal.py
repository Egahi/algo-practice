'''
https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/786/
'''
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        output = []
        nodes = []
        cursor = root

        while cursor or nodes:
            while cursor:
                nodes.append(cursor)
                cursor = cursor.left
            
            cursor = nodes.pop()
            output.append(cursor.val)
            cursor = cursor.right

        return output
            
        # self.output = []

        # def inorderTraversal(node):
        #     if not node:
        #         return

        #     if node.left:
        #         inorderTraversal(node.left)

        #     self.output.append(node.val)

        #     if node.right:
        #         inorderTraversal(node.right)

        # inorderTraversal(root)
        # return self.output

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
obj = Solution()
print(obj.inorderTraversal(root))