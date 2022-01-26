
class Solution(object):

    def canJump(self, nums: list) -> bool:

        reachable = 0

        for idx, length in enumerate(nums):


            print(f'index: {idx}')
            print(f'length: {length}')
            print(f'reachable: {reachable}')

            if idx > reachable:
                break
            print(f'idx + length: {idx + length}')
            reachable = max(reachable, idx + length)
            print(f'new reacheble: {reachable}')
            print('\n')

        return reachable >= len(nums) - 1


if __name__ == '__main__':


    nums = [2,3,1,1,4]
    print(Solution().canJump(nums=nums))



            