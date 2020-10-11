


class Solution:

    def maxArea(self, height):

        # start with no area
        max_area = 0 
        # set the moving point at zero
        idx = 0
        # set threshold at which line is slanted
        jdx = len(height) - 1

        # train moving point to meet point of max area
        while idx < jdx:
            # define max areals
            max_area = max(max_area, min(height[idx], height[jdx]) * (jdx -  idx))
            print(f'Current Max Area: {max_area}\n')
            # set unit of learning by condition of line
            if height[idx] < height[jdx]:
                idx += 1
            else:
                jdx -= 1

        print(f'Final Max Area: {max_area}\n')

        return max_area