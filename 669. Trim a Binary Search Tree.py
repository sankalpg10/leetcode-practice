# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        self.low = low
        self.high = high
        def traverseAndTrim(node):
            if not node: return None
            if node.val < self.low: return traverseAndTrim(node.right)
            if node.val > self.high: return traverseAndTrim(node.left)
            node.left = traverseAndTrim(node.left)
            node.right = traverseAndTrim(node.right)
            return node
        return traverseAndTrim(root)
