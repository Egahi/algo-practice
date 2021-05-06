'''
https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/787/
'''
from typing import List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        nodes, output = deque([(root, 0)]), []
        
        temp, level, isReverse = deque(), 0, False

        while nodes:
            node = nodes.popleft()

            if node[1] == level:
                if isReverse:
                    temp.appendleft(node[0].val)
                else:
                    temp.append(node[0].val)
            else:
                output.append(temp)
                temp = deque([node[0].val])
                level += 1
                isReverse = not isReverse
                
            if node[0].left:
                nodes.append((node[0].left, node[1]+1))

            if node[0].right:
                nodes.append((node[0].right, node[1]+1))

        output.append(temp)

        return output

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
obj = Solution()
print(obj.zigzagLevelOrder(root))