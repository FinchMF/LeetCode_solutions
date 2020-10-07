class Solution:
    def twoSum(self, arr, target):
        arr_dict = {}
        for idx in range(len(arr)):
            if target - arr[idx] in arr_dict:
                return [arr_dict[target - arr[idx]], idx]
            arr_dict[arr[idx]] = idx
    