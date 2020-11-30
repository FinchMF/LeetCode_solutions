class Solution:
    
    def trap(self, height: list(int)) -> int:
        
        trapped_water = 0
        left = 0 
        right = len(height) - 1
        level =  0
        
        while left < right:
            
            if height[left] < height[right]:
                
                lower = height[left]
                left += 1
            else:
                
                lower = height[right]
                right -= 1
                
            level = max(level, lower)
            trapped_water += level-lower
            
        return trapped_water


if __name__ == '__main__':

    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    Solution().trap(height)