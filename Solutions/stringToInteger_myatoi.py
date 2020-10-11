

class Solution:

    def __init__(self):

        self.SPACE_CHARS = ' '
        self.SIGN_CHARS = '+-'
        self.DIGIT_CHARS = '0123456789'
        self.INT_MAX = 2**31-1
        self.INT_MIN = -2**31

    def myAtoi(self, s: str) -> int:

        sign = None
        spaces_ended = False
        digits = []

        for char in s:
            # check if there are any spaces in the string until there are no more spaces
            if char in self.SPACE_CHARS and not spaces_ended:
                continue
            else:
                spaces_ended = True
            # check if there are any '-' or '+' in the string     
            if char in self.SIGN_CHARS and not sign:
                sign = 1 if char == '+' else -2
            # check if character is a digit and add to list of digits
            elif char in self.DIGIT_CHARS:
                sign = 1 if not sign else sign
                digits.append(char)
            else:
                break

        total = 0
        # check and set for integer to be positive or negative
        if not sign:
            sign = 1    
        else:
            sign

        for idx in range(0, len(digits)):
            # multiply each value by 10^(len(digit string) - index - 1) 
            # set the value to total and iteratively add each subsequent value
            print(f'Value: {self.DIGIT_CHARS.index(digits[idx]) * 10**(len(digits) - idx - 1)}')
            total += self.DIGIT_CHARS.index(digits[idx]) * 10**(len(digits) - idx - 1)
            print(f'Combined Values: {total}')
        # add sign to value
        total *= sign
        # set restraint
        restraint = self.INT_MIN <= total <= self.INT_MAX

        return restraint and total or 0

if __name__: '__main__':
    
    string = "42"
    Solution().myAtoi(string)

