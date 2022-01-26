
class Solution(object):

    def canJump(self, nums: list) -> bool:

        reachable = 0

        for idx, length in enumerate(nums):

            if idx > reachable:
                break

            reachable = max(reachable, idx + length)

        return reachable >= len(nums) - 1


if __name__ == '__main__':


    nums = [2,3,1,1,4]
    print(Solution().canJump(nums=nums))



            