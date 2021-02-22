# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root: return []
        valcounts = collections.defaultdict(int)
        def getMode(node):
            if node is None: return
            valcounts[node.val] += 1
            getMode(node.left)
            getMode(node.right)
        
        getMode(root)
        modes = []
        maxValCounts = max([valcounts[val] for val in valcounts])
        print(maxValCounts, valcounts)
        return [val for val in valcounts if valcounts[val] == maxValCounts]
