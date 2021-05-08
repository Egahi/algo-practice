'''
https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/791/
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        successor = None

        while root:
            if p.val >= root.val:
                root = root.right
            else:
                successor = root
                root = root.left

        return successor


#[6,2,8,0,4,7,9,null,null,3,5]
#2
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)
obj = Solution()
print(obj.inorderSuccessor(root, root.left).val)