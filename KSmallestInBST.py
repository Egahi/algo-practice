'''
https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/790/
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        nodes = []
        while True:
            while root:
                nodes.append(root)
                root = root.left

            root = nodes.pop()
            k -= 1

            if not k:
                return root.val
                
            root = root.right

root = TreeNode(1)
k = 1
obj = Solution()
print(obj.kthSmallest(root, k))