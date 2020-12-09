
from typing import List

class Solution:

    def jump(self, nums: List[int]) -> int:
        
        curr_max_dist = 0
        jumps = 0
        max_idx = 0
        
        for i in range(len(nums)-1):
            
            max_idx = max(max_idx, i+nums[i])
            
            if curr_max_dist == i:
                
                curr_max_dist = max_idx
                
                if curr_max_dist > i:
                    
                    jumps += 1
                else:
                    
                    return -1
                
        return jumps

if __name__ == '__main__':

    nums = [2,3,1,1,4]
    Solution().jump(nums)