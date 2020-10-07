class Solution:
    def twoSum(self, nums, target):
        num_dict = {}
        for idx in range(len(nums)):
            if target - nums[idx] in num_dict:
                return [num_dict[target - nums[idx]], idx]
            num_dict[nums[idx]] = idx
    