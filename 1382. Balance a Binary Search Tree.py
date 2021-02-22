# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        nodevals = []
        def dfs(node):
            if not node: return
            dfs(node.left)
            nodevals.append(node.val)
            dfs(node.right)
        
        def makeBST(vals, left, right):
            if left >= right: return
            mid = left + (right - left)//2
            node = TreeNode(val=vals[mid])
            node.left = makeBST(vals, left, mid)
            node.right = makeBST(vals, mid+1, right)
            return node
        
        dfs(root)
        return makeBST(nodevals, 0, len(nodevals))
