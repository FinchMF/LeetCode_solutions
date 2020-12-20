
from typing import List

class Solution:

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        for idx, x in enumerate(nums2):

            nums1[idx+m] = nums2[idx]

        nums1.sort()



if __name__ == '__main__':

    nums1 = [1,2,3,0,0,0] 
    m = 3

    nums2 = [2,5,6]      
    n = 3    

    print(f' Input Arr One: {nums1}')
    print(f' Input Arr Two: {nums2}')
    (Solution().merge(nums1, m, nums2, n))
    print(f'Merge Sorted Arr Output: {nums1}')