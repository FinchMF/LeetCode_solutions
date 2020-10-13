

class Solution:

    def threeSumClosest(self, nums, target):

        res = diff = float('inf')
        nums.sort()

        for idx in range(len(nums)):

            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue

            l, r = idx + 1, len(nums) - 1

            while l < r:

                x = nums[idx] + nums[l] + nums[r]

                if abs(x - target) < diff:

                    diff = abs(x - target)
                    res = x

                if x < target:
                    l += 1

                elif x > target:
                    r -= 1

                else:
                    return res

        return res

if __name__ == '__main__':

    nums = [-1,2,1,-4]
    target = 1

    Solution().threeSumClosest(nums, target)