from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        """Iterative pre-order DFS, extract all values, sort and return k - 1th element.
        Optimal solution would be in-order DFS traversal, will get around to implementing this.
        Runtime: 56 ms, faster than 41.94%
        Memory Usage: 18.1 MB, less than 57.08%
        """
        if root is None:
            return root

        count = 0
        queue = deque([root])
        all_vals = []
        while queue:
            node = queue.popleft()
            all_vals.append(node.val)
            if node.right:
                queue.appendleft(node.right)
            if node.left:
                queue.appendleft(node.left)
        return sorted(all_vals)[k - 1]
