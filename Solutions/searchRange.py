
import bisect

class Solution:

    def searchRange(self, nums, target):

        left, right = bisect.bisect_left(nums, target), bisect.bisect_right(nums, target) - 1

        return [left, right] if 0 <= left <= right else [-1,-1]


if __name__ == '__main__':

    nums, target = [5,7,7,8,8,10], 8
    Solution().searchRange(nums, target)