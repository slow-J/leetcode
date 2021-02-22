"""You are given two linked-lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def ll_to_num(self, node):
        total = 0
        i = 1
        while node:
            total += node.val * i
            i *= 10
            node = node.next
        return total

    def num_to_ll(self, num):
        node = dummy = ListNode(-1)
        for char in str(num)[::-1]:
            node.next = ListNode(int(char))
            node = node.next
        return dummy.next

    def addTwoNumbers(self, l1, l2, c=0):
        if not l1 and not l2:
            return 0
        if not l1:
            return l2
        if not l2:
            return l1
        c = self.ll_to_num(l1) + self.ll_to_num(l2)
        return self.num_to_ll(c)


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
    print(result.val)
    result = result.next
# 7 0 8
