
class Solution:

    def generateParenthesis(self, n):

        bfs = [(0,0, '')]

        for c in range(n * 2):
            bfs = [(l + 1, r, s + '(') for l, r, s in bfs if l + 1 <=n] + [(l, r + 1, s + ')') for l, r, s in bfs if l -r]
        
        return [s for l, r, s in bfs]


if __name__ == '__main__':

    n = 3

    Solution().generateParenthesis(n)

    