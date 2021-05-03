'''
https://leetcode.com/explore/interview/card/top-interview-questions-medium/107/linked-list/785/
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pA, pB = headA, headB

        while pA != pB:
            pA = headB if pA is None else pA.next
            pB = headA if pB is None else pB.next

        return pA

headA = ListNode(4)
headA.next = ListNode(1)
headA.next.next = ListNode(8)
headA.next.next.next = ListNode(4)
headA.next.next.next.next = ListNode(5)

headB = ListNode(5)
headB.next = ListNode(6)
headB.next.next = ListNode(1)
headB.next.next.next = headA.next.next
headB.next.next.next.next = ListNode(4)
headB.next.next.next.next.next = ListNode(5)

obj = Solution()
print(obj.getIntersectionNode(headA, headB).val)