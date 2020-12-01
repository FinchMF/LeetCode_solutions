
class Solution:

    def permute(self, nums: list(int)) -> list(list(int)):
        
        n = len(nums)
        
        if n == 0:
            return [[]]
        
        perms = []
        for i in range(n):
            
            for p in self.permute(nums[:i] + nums[i+1:]):
                
                perms.append([nums[i]] + p)
                
        return perms


if __name__ == '__main__':

    nums = [1,2,3]
    Solution().permute(nums)

