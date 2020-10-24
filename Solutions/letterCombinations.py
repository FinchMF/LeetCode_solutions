

class Solution:

    def letterCombinations(self, digits):

        keypad_dic = {

            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        result = ['']

        for digit in digits:
            # set temporary empty list
            # also erase pevious temp list after each iteration
            temp = []
            # reference letters currently in result iteratively 
            for y in result:
                # make combiation of current letter in result digit's dict value
                for x in keypad_dic[digit]:
                    temp.append(y + x)
                result = temp
        
        return result if any(result) else []



if __name__ == '__main__':

    digits = '23'
    Solution().letterCombinations(digits)

