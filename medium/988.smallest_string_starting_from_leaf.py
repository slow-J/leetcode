# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
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


class Solution2:
    """Iterative DFS with 1 queue of tuples. Better memory usage than BFS.
    Runtime: 40 ms, faster than 94.41%
    Memory Usage: 15.6 MB, less than 78.26%
    """

    def smallestFromLeaf(self, root: TreeNode) -> List[str]:
        if not root:
            return root
        stack = deque([(root, "")])
        found_paths = deque()
        while stack:
            cur_node, paths = stack.popleft()
            new_string = chr((cur_node.val) + 97) + paths
            if cur_node.right:
                stack.appendleft((cur_node.right, new_string))
            if cur_node.left:
                stack.appendleft((cur_node.left, new_string))
            if not cur_node.left and not cur_node.right:
                found_paths.append(new_string)

        smallest_path = None
        for path in found_paths:
            if not smallest_path:
                smallest_path = path
            else:
                smallest_path = min(path, smallest_path)
        return smallest_path
