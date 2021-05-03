'''
https://leetcode.com/explore/interview/card/top-interview-questions-medium/107/linked-list/783/
'''

#Definition for singly-linked list.
from typing import List
import timeit


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        Iterative solution
        '''
        output = ListNode(0)
        cursor = output
        carry = 0

        while l1 or l2 or carry:
            sum = 0

            if l1:
                sum += l1.val
                l1 = l1.next
            
            if l2:
                sum += l2.val
                l2 = l2.next

            sum += carry
            carry = sum // 10
            cursor.next = ListNode(sum % 10)
            cursor = cursor.next

        return output.next
    
    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        Recursive solution
        '''
        def addTwoNumbers(l1, l2, carry):
            if not l1 and not l2:
                if carry:
                    return ListNode(carry)
                else:
                    return

            sum = 0

            if l1:
                sum += l1.val
                l1 = l1.next
            
            if l2:
                sum += l2.val
                l2 = l2.next

            sum += carry

            output = ListNode(sum % 10)
            carry = sum // 10

            output.next = addTwoNumbers(l1, l2, carry)

            return output

        return addTwoNumbers(l1, l2, 0)

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

obj = Solution()
print(obj.addTwoNumbers(l1, l2))
print(obj.addTwoNumbers2(l1, l2))

#print(timeit.timeit('"-".join(str(n) for n in range(100))', number=10000))