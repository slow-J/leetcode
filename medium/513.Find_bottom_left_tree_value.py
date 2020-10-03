# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def recursive_max_depth(node, depth):
    """Returns a tuple of max_depth, deepest_left_val"""
    if node.left is None and node.right is None:
        return depth, node.val
    if node.left is None:
        return recursive_max_depth(node.right, depth + 1)
    if node.right is None:
        return recursive_max_depth(node.left, depth + 1)
    left_depth, left_val = recursive_max_depth(node.left, depth + 1)
    right_depth, right_val = recursive_max_depth(node.right, depth + 1)
    if left_depth < right_depth:
        return right_depth, right_val
    else:
        return left_depth, left_val


class Solution:
    def findBottomLeftValue(self, root):
        """def findBottomLeftValue(self, root: TreeNode) -> int:"""
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return root.val
        if root.left is None:
            right_depth, right_val = recursive_max_depth(root.right, 2)
            return right_val
        if root.right is None:
            left_depth, left_val = recursive_max_depth(root.left, 2)
            return left_val

        left_depth, left_val = recursive_max_depth(root.left, 2)
        right_depth, right_val = recursive_max_depth(root.right, 2)
        print(left_depth, left_val)
        print(right_depth, right_val)
        if left_depth < right_depth:
            return right_val
        else:
            return left_val
