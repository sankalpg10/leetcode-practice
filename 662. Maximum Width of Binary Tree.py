# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        
        q = collections.deque([(root, 0)])
        max_width = 0
        while q:
            total_nodes_at_currLevel = len(q)
            _, level_of_first_node = q[0]
            for _ in range(total_nodes_at_currLevel):
                node, col_index = q.popleft()
                if node.left:
                    q.append((node.left, 2*col_index))
                if node.right:
                    q.append((node.right, 2*col_index+1))
            
            max_width = max(max_width, col_index - level_of_first_node + 1)

        return max_width
