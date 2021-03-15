
class Solution:
    
    def mySqrt(self, x: int) -> int:

        if x < 0:
            return 0
        else:
            return int(x**(1/2))


if __name__ == '__main__':

    for x in range(-1,30):
        print(Solution().mySqrt(x))