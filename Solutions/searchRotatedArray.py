
class Solution:

    def search_arr(self, nums, target):

        l, r = 0, len(nums) - 1

        while l <= r:

            mid = (l + r) // 2

            if nums[mid] == target:

                return mid

            elif sum((target < nums[l], nums[l] <= nums[mid], nums[mid] < target)) == 2:

                l = mid + 1
            else: 
                r = mid - 1

        return -1


if __name__ == '__main__':

    nums, target = [4,5,6,7,0,1,2], 0
    Solution().search_arr(nums, target)

