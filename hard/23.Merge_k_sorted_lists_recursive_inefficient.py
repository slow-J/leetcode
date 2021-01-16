# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKListsRec(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists == []:
            return None

        lowest_head_pos = 0
        lowest_head_val = lists[0].val
        lowest_head = lists[0]
        for i, head in enumerate(lists):
            if head.val < lowest_head_val:
                lowest_head = head
                lowest_head_val = head.val
                lowest_head_pos = i
        if lists[lowest_head_pos].next is None:
            lists.pop(lowest_head_pos)
        else:
            lists[lowest_head_pos] = lists[lowest_head_pos].next
        lowest_head.next = self.mergeKListsRec(lists)
        return lowest_head

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists == []:
            return None
        lists = list(filter(None, lists))
        return self.mergeKListsRec(lists)
