# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head.next is None:
            return head
        if m == n:
            return head

        ll_rest_right = current = head
        ll_rest_left = None

        # Iterate current node to first node that will be rotated.
        for x in range(m - 1):
            if x == m - 2:
                # Last node to the left of the rotated section.
                ll_rest_left = current
            current = current.next

        # ll_rest_right is the first node (or None) to the right of rotated section.
        for _ in range(n):
            ll_rest_right = ll_rest_right.next

        prev = ll_rest_right
        for _ in range(n + 1 - m):
            next = current.next
            current.next = prev
            prev = current
            current = next

        # If rotating from 1st node, there is no node before the rotated section.
        if (m == 1):
            head = prev
        else:
            ll_rest_left.next = prev
        return head
