# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        Trivial BFS
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        lists = []
        queue, current = [root], []
        while queue:
            current, queue = queue, []
            inner_list = []
            for elem in current:
                inner_list.append(elem.val)
                if elem.left:
                    queue.append(elem.left)
                if elem.right:
                    queue.append(elem.right)
            lists.append(inner_list)
        return lists[::-1]
