# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        
        def traverseAndInsert(node):
            if not node: return
            
            if node.val > val:
                if node.left == None: 
                    node.left = TreeNode(val)
                    return
                traverseAndInsert(node.left)
                
            else: 
                if node.right == None: 
                    node.right = TreeNode(val)
                    return
                traverseAndInsert(node.right)
            
            
        traverseAndInsert(root)
        return root
            
            
