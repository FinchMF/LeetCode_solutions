
class Solution:

    def removeElement(self, nums, val):

        i = 0 

        for n in nums:

            if n != val:
                nums[i] = n

                i +=1

        return i 


if __name__ == '__main__':

    nums, val = [3,2,2,3], 3
    Solution().removeElement(nums, val)