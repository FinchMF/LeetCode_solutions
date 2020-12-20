
from typing import List

class Solution:

    def maxSubArray(self, nums: List[int]) -> int:

        if nums == None or nums == 0: return None

        max_curr = [nums[0]]

        for idx in range(1, len(nums)):

            max_curr.append(max(nums[idx], nums[idx]+max_curr[-1]))

        return max(max_curr)


if __name__ == '__main__':

    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(Solution().maxSubArray(nums))