

class Solution(object):

    def findLonely(self, nums: list) -> list:

        counter = {}

        for n in nums:

            if n in counter:

                counter[n]['number'] += 1
            else:
                counter[n] = {

                    'number': 1, 
                    'neighbors': False
                }

            neighbor_left = (n - 1) in nums
            neighbor_right = (n + 1) in nums

            if neighbor_left or neighbor_right:

                counter[n]['neighbors'] = True


        lonely = []

        for n, details in counter.items():

            if details['number'] == 1:
                lonely.append(n)

            if details['neighbors'] == False:
                lonely.append(n)


        return lonely


if __name__ == '__main__':

    nums = [10,6,5,8]
    print(Solution().findLonely(nums=nums))



 
        



