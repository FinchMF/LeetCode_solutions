
class Solution:

    def divide(self, dividend: int, divisor: int) -> int:

        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor, result = abs(dividend), abs(divisor), 0

        while dividend >= divisor:

            temp, i = divisor, 1

            while dividend >= temp:
                dividend -= temp
                result += i
                i <<= 1
                temp <<= 1

        if not positive: result = -result

        return min(max(-2**31, result), 2**31-1)



if __name__ == '__main__':

    dividend, divisor = 10, 3

    Solution().divide(dividend, divisor)