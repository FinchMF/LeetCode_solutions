from typing import List

class Solution:
    def plusOne(self, digits: List[int] ) -> List[int]:
        digits = [ str(n) for n in digits ]
        digits = int(''.join(digits)) + 1
        return [ int(n) for n in str(digits) ]


if __name__ == '__main__':

    number = [1,8,9,9]
    print(Solution().plusOne(digits=number))