# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None:
            return TreeNode(val)
        root_copy = root
        inserted = False
        while not inserted:
            if root.val < val:
                if root.right is not None:
                    root = root.right
                else:
                    root.right = TreeNode(val)
                    inserted = True
            else:
                if root.left is not None:
                    root = root.left
                else:
                    root.left = TreeNode(val)
                    inserted = True
        return root_copy
