class Solution:

    def reverse(self, x):

        if x >=0:
            # reverse the digits's order via indice reversal
            x = int(str(x)[::-1])
        
        else:
            # reverse digits and add a negative sign
            int('-' + str(x)[::-1][:-1])
        # address the threshold specified in the question
        restraint = ( -2**31 ) <= x <= ( 2**31 - 1)

        return restraint and x or 0

        