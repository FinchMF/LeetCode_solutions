from typing import List
from collections import defaultdict

class Solution:
    
    def firstMissingPositive(self, nums: List[int]) -> int:
         
        d = defaultdict(int)
        for i in nums:
            d[i] = 1

        j = 1
        while True:
            if d[j] == 0:
                return j
            j += 1


if __name__ == '__main__':

    nums = [1,2,0]
    Solution().firstMissingPositive(nums)