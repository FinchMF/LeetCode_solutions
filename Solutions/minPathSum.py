
from typing import List

class Solution:
    
    def minPathSum(self, grid: List[List[int]]) -> int:
    
        sm = list(grid[0])
        for j in range(1, len(grid[0])):

            sm[j] = sm[j-1] + grid[0][j]
            
        for i in range(1, len(grid)):

            sm[0] += grid[i][0]
            for j in range(1, len(grid[0])):

                sm[j] = min(sm[j-1], sm[j]) + grid[i][j]
                
        return sm[-1]

if __name__ == '__main__':

    grid = [[1,3,1],[1,5,1],[4,2,1]]
    Solution().minPathSum(grid)

