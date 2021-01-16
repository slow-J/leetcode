import Queue as Q
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists == []:
            return None
        # lists = list(filter(None, lists))
        q = Q.PriorityQueue()
        for node in lists:
            while node is not None:
                q.put(node.val)
                node = node.next
        # q.put(x.val) for x in list for list in lists
        dummy_node = ll_node = ListNode(0)
        while not q.empty():
            ll_node.next = ListNode(q.get())
            ll_node = ll_node.next

        return dummy_node.next
