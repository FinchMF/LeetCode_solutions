

class Solution:
    def isMatch(self, string: str, pattern: str) -> bool:

        result = [[False for jdx in range(len(pattern) + 1)] for idx in range(len(string) + 1)]

        result[0][0] = True 

        for idx in range(2, len(pattern) + 1):
            if pattern[idx - 1] == '*':
                result[0][idx] = result[0][idx - 2]

        for idx in range(1, len(string) + 1):
            for jdx in range(1, len(pattern) + 1):
                if pattern[jdx - 1] != '*':
                    result[idx][jdx] = result[idx - 1][jdx - 1] and (string[idx - 1] == pattern[jdx - 1] == '.')
                else:
                    result[idx][jdx] = result[idx][jdx - 2] or (result[idx - 1][jdx] and (string[idx - 1] == pattern[jdx - 2] or pattern[jdx - 2] == '.'))

        return result[len(string)][len(pattern)]

        

