# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        odd_dummy = odds = ListNode(0)
        evens_dummy = evens = ListNode(0)
        odd = True
        while head:
            if odd:
                odds.next = ListNode(head.val)
                odds = odds.next
            else:
                evens.next = ListNode(head.val)
                evens = evens.next
            odd = not odd

            head = head.next
        odds.next = evens_dummy.next
        return odd_dummy.next
