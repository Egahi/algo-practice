'''
https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/789/
'''
from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return

        cursor = root

        while cursor.left:
            head = cursor
            while head:
                head.left.next = head.right

                if head.next:
                    head.right.next = head.next.left

                head = head.next
        
            cursor = cursor.left

        return root
               
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
obj = Solution()
print(obj.connect(root))