# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def recursive_max_depth(node, depth):
    if node.left is None and node.right is None:
        return depth
    if node.left is None:
        return recursive_max_depth(node.right, depth + 1)
    if node.right is None:
        return recursive_max_depth(node.left, depth + 1)
    return max(recursive_max_depth(node.left, depth + 1), recursive_max_depth(node.right, depth + 1))


class Solution:
    def maxDepth(self, root):
        """maxDepth(self, root: TreeNode) -> int:"""
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        if root.left is None:
            return recursive_max_depth(root.right, 2)
        if root.right is None:
            return recursive_max_depth(root.left, 2)
        return max(recursive_max_depth(root.left, 2), recursive_max_depth(root.right, 2))
