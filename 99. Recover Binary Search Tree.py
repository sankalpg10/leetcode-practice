# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        """
              3
             / \
            1   4 (2, 2), (5, 5)
               / \
              2   5 
   (None, None)   (None, None)
        """
        
        pred, x, y = None, None, None
        def dfs(node):
            if not node: return
            dfs(node.left)
            nonlocal x, y, pred
            if pred and node.val < pred.val:
                y = node # 1
                if not x:
                    x = pred # 3
                else:
                    return
                
            pred = node # 1
            dfs(node.right) 
            
        dfs(root)
        x.val, y.val = y.val, x.val # 1, 3 = 3, 1
