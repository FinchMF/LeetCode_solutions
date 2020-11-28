
class Solution:
    def rotate(self, matrix: list(list(int))) -> None:

        N = len(matrix[0])
        
        for i in range(N // 2):
            
            for j in range(i, N - i - 1):
                
                tmp = matrix[i][j]
                
                matrix[i][j] = matrix[N - 1 - j][i]
                
                matrix[N - 1 - j][i] = matrix[N - 1 -i][N -1 -j]
                
                matrix[N - 1 - i][N - 1 - j] = matrix[j][N - 1 -i]
                
                matrix[j][N - 1 - i] = tmp
                
        return None



if __name__ == '__main__':

    matrix = [[1,2,3],
              [4,5,6],
              [7,8,9]]

    Solution().rotate(matrix)