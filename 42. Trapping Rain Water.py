class Solution:
    def trap(self, height: List[int]) -> int:
        
        left, right = 0, len(height)-1
        leftWall, rightWall = 0, 0
        trappedWater = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] > leftWall: 
                    leftWall = height[left]
                else:
                    trappedWater += leftWall - height[left]
                left += 1
            else:
                if height[right] > rightWall:
                    rightWall = height[right]
                else:
                    trappedWater += rightWall - height[right]
                right -= 1
                
        return trappedWater
