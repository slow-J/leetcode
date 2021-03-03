# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """Iterative BFS with 1 queue of tuples.
    Runtime: 32 ms, faster than 99.79%
    Memory Usage: 15.8 MB, less than 13.25%
    """

    def smallestFromLeaf(self, root: TreeNode) -> List[str]:
        if not root:
            return root
        stack = deque([(root, "")])
        found_paths = deque()
        while stack:
            cur_node, path = stack.popleft()
            new_path = chr((cur_node.val) + 97) + path
            if cur_node.left:
                stack.append((cur_node.left, new_path))
            if cur_node.right:
                stack.append((cur_node.right, new_path))
            if not cur_node.left and not cur_node.right:
                found_paths.append(new_path)

        smallest_path = None
        for path in found_paths:
            if not smallest_path:
                smallest_path = path
            else:
                smallest_path = min(path, smallest_path)
        return smallest_path
