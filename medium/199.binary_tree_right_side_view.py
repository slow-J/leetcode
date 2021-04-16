from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return root
        queue, current = deque([root]), deque()
        rights = []
        while queue:
            current, queue = queue, current
            while current:
                tmp = current.popleft()
                if len(current) == 0:
                    rights.append(tmp.val)
                if tmp.left:
                    queue.append(tmp.left)
                if tmp.right:
                    queue.append(tmp.right)
        return rights
