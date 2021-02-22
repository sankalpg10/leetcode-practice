class Solution:
    def findTilt(self, root: TreeNode) -> int:
        
        def getTilt(node):
            if not node: return (0, 0)
            
            leftTilt, leftSum = getTilt(node.left)
            rightTilt, rightSum = getTilt(node.right)
            currTotalTilt = (abs(leftSum - rightSum) + leftTilt + rightTilt)
            currSum = leftSum + rightSum + node.val
            return  (currTotalTilt, currSum)
        
        
        return getTilt(root)[0]
