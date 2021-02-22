# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        closest = inf
        
        minAbs = lambda x, y:  x if abs(x-target) < abs(y-target) else y
        node = root
        while node:
            
            closest = minAbs(node.val, closest)
            if node.val > target:
                node = node.left
            else:
                node = node.right
                
        return closest
