# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """March LeetCoding Challenge 2021 week 2.
    BFS (again)
    Runtime: 48 ms  faster than 93.90%
    Memory Usage: 16.3 MB  less than 79.05%"""
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            top = TreeNode(v)
            top.left = root
            return top
        queue, current = [root], []
        depth = 1
        while queue:
            queue, current = [], queue
            for node in current:
                if depth == d - 1:
                    tmp = TreeNode(v)
                    node.left, tmp.left = tmp, node.left
                    tmp = TreeNode(v)
                    node.right, tmp.right = tmp, node.right
                else:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            depth += 1
        return root
