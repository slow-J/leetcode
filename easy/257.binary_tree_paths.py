# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """Iterative BFS with 1 queue.
    Runtime: 28 ms, faster than 90.33%
    Memory Usage: 14 MB, less than 95.45%
    """

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return root
        stack = deque([(root, "")])
        current = deque()
        found_paths = []

        while stack:
            cur_node, paths = stack.popleft()
            if cur_node.left:
                if not paths:
                    stack.append((cur_node.left, str(cur_node.val)))
                else:
                    stack.append((cur_node.left, paths + "->" + str(cur_node.val)))
            if cur_node.right:
                if not paths:
                    stack.append((cur_node.right, str(cur_node.val)))
                else:
                    stack.append((cur_node.right, paths + "->" + str(cur_node.val)))
            if not cur_node.left and not cur_node.right:
                if not paths:
                    found_paths.append(str(cur_node.val))
                else:
                    found_paths.append(paths + "->" + str(cur_node.val))

        return found_paths
