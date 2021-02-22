# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        """
        Rob(node) = max amount possible at that node
        
        Base case:
        Rob(node) = 0 if not node
        
        general case
        Rob(node) = max(node.val + Rob(node.next.next) (if not none), Rob(node.next))
        
        """
        memo = {}
        def Rob(node):
            if not node: return 0
            if node in memo: return memo[node]
            robNowLeft = 0 if node.left is None else Rob(node.left.left) + Rob(node.left.right)
            robNowRight = 0 if node.right is None else Rob(node.right.left) + Rob(node.right.right)
            robNow = robNowLeft + robNowRight + node.val
            skipNow = Rob(node.left) + Rob(node.right)
            memo[node] = max(robNow, skipNow)
            
            return memo[node]
                
        return Rob(root)
