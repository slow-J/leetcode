# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def ll_to_list(head):
    ret_list = []
    while head:
        ret_list.append(head.val)
        head = head.next
    return ret_list


class Solution:
    def sortList(self, head):
        # def sortList(self, head: ListNode) -> ListNode:
        new_head = ListNode(0)
        head_copy = new_head
        unsorted_list = ll_to_list(head)
        for val in sorted(unsorted_list):
            head_copy.next = ListNode(val)
            head_copy = head_copy.next
        return new_head.next
