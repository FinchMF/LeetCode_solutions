
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        if not matrix:
            return []

        result = []
        m, n = len(matrix), len(matrix[0])
        layers = (min(m, n) + 1) // 2

        
        for l in range(layers):
           
            for i in range(l, n-l):
                result.append(matrix[l][i])
           
            for i in range(l+1, m-l):
                result.append(matrix[i][n-l-1])
          
            if l < m - l - 1:
                for i in range(n-l-2, l, -1):
                    result.append(matrix[m-l-1][i])
           
            if l < n - l - 1:
                for i in range(m-l-1, l, -1):
                    result.append(matrix[i][l])

        return result

if __name__ == '__main__':

    M1x3 = [[7],
            [6],
            [9]]

    M3x3 = [[1,2,3],
           [4,5,6],
           [7,8,9]]

    M3x4 = [[1,2,3,4],
           [5,6,7,8],
           [9,10,11,12]]



    matrices = [M1x3, M3x3, M3x4]

    for matrix in matrices:
        
        Solution().spiralOrder(matrix)