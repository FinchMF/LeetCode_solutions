class Solution:
    def convert(self, s, n_rows):

        if n_rows == 1 or n_rows >= len(s): return s

        row = 0
        direction = -1
        result = [''] * n_rows

        for ele in s:
            
            result[row] += ele
            if row == 0 or row == n_rows - 1: direction *= -1
            row += direction
            
            print(f'element: {ele} in row: {row}')
        print('\n')
        print('RESULT:')

        return ''.join(result)
