

class Solution:

    def threeSum(self, nums):

        res = []
        res_start = set()
        nums.sort()

        for idx in range(len(nums) - 2):

            l, r = idx +1, len(nums) - 1

            while l < r:

                x = nums[idx] + nums[l] + nums[r]

                if x < 0:
                    l += 1
                elif x > 0:
                    r -= 1

                elif (nums[idx], nums[l], nums[r]) not in res_start:

                    res.append([nums[idx], nums[l], nums[r]])
                    res_start.add((nums[idx], nums[l], nums[r]))
                
                else:
                    l, r = l + 1, r - 1

        return res


if __name__ == '__main__':

    nums = [-1,0,1,2,-1,-4]
    Solution().threeSum(nums)