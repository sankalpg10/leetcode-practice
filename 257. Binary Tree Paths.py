# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root: return []
        allPaths = []
        def traverseAndAccumulate(node, currPath):
            nonlocal allPaths
            
            if node.left == None and node.right == None:
                allPaths.append("->".join(currPath+[str(node.val)]))
                return    
            if node.left != None: traverseAndAccumulate(node.left, currPath+[str(node.val)])
            if node.right != None: traverseAndAccumulate(node.right, currPath+[str(node.val)])
            
        traverseAndAccumulate(root, [])
        return allPaths
