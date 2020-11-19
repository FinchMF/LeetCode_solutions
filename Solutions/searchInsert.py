
import bisect

class Solution:

    def searchInsert(self, nums, target):

        return bisect.bisect_left(nums, target)



if __name__ == '__main__':

    nums, target = [1,3,5,6], 5
    Solution().searchInsert(nums, target)