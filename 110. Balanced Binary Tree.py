# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n), O(H)
class Solution:
    
    def isBalanced(self, root: TreeNode) -> bool:
        self.isBalanced = True
        self.height(root)

        return self.isBalanced

    def height(self, node):
        if not node: return 0 

        left = self.height(node.left)
        right = self.height(node.right)
        if abs(left - right) > 1: self.isBalanced = False
        return max(left, right) + 1

"""
O(nlogn), O(H)
class Solution1:
    
    def isBalanced(self, root: TreeNode) -> bool:
        if not root: return True
      
        leftheight = self.height(root.left, 1)
        rightheight = self.height(root.right, 1)
        isRootBalanced = leftheight == rightheight or abs(leftheight - rightheight) == 1
      
        return isRootBalanced and isBalanced(root.left) and isBalanced(root.right)
      
      
    def height(self, node, curr_height):
        if not node:
            return curr_height
        return max(self.height(node.left, curr_height+1), self.height(node.right, curr_height+1))
"""
