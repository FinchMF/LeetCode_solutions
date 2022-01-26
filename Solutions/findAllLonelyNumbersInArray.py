import collections

class Solution(object):

    def findLonely(self, nums: list) -> list:

        counter = collections.Counter(nums)
        return [n for n in nums if counter[n] == 1 and n-1 not in counter and n+1 not in counter]

if __name__ == '__main__':

    nums = [10,6,5,8]
    print(Solution().findLonely(nums=nums))



 
        



