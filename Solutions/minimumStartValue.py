
class Solution:

    def minimum_start_value(self, arr):

        x = 1
        s = 0
        size = arr[0]

        for n in arr[::-1][:-1]:

                if n > 0:

                    s -= n
                    continue
                if n < 0:

                    s += abs(n)
                    continue
                if s < 1:

                    break
                if s >=1:

                    x += s
                    return x
        x += s
        return x


if __name__ == '__main__':

    arrs = [[4,-2,3,1,-5], [10, -5, 4, -2, 3, 1, -1, -6, -1, 0, -5]]

    for arr in arrs:

        Solution().minimum_start_value(arr)