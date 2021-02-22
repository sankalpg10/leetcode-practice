# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        
        if root is None: return 0
        numUniSubTrees = 0
        def dfs(node):
            nonlocal numUniSubTrees
            if node.left is None and node.right is None:
                numUniSubTrees += 1
                return True
            
            is_uni = True
            
            if node.left is not None:
                is_uni = dfs(node.left) and node.left.val == node.val
                
            if node.right is not None:
                is_uni = dfs(node.right) and is_uni and node.right.val == node.val
            
            numUniSubTrees += is_uni
            return is_uni
        
        dfs(root)
        return numUniSubTrees

# similar solution but a bit ugly
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        numSubTrees = 0
        
        def dfs(node):
            if not node: return (True, None)
            nonlocal numSubTrees
            isUniValuedL, lval = dfs(node.left)
            isUniValuedR, rval = dfs(node.right)
            
            if (lval is None and rval == node.val and isUniValuedR) or (rval is None and lval == node.val and isUniValuedL) or (isUniValuedL and isUniValuedR and node.val == rval == lval) or (lval is None and rval is None):
                numSubTrees += 1
                return (True, node.val)
            
            return (False, node.val)
                
        dfs(root)
        return numSubTrees
