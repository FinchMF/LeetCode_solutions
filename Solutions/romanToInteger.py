class Solution:
    def romanToInt(self, s: str) -> int:
        
        # set look up table: roman -> int
        num_lkup = {

            "I": 1, 
            "V": 5, 
            "X": 10, 
            "L": 50, 
            "C":100, 
            "D": 500, 
            "M": 1000
            
            }

        n = 0

        for i in range(len(s)):
            print(f'i = {i}')
            if i > 0 and num_lkup[s[i]] > num_lkup[s[i - 1]]:
                n += num_lkup[s[i]] - (2 * num_lkup[s[i - 1]])
                print(f'N _ 1 = {n}')
            else:
                n += num_lkup[s[i]]
                print(f'N _ 2 = {n}')
                
        print(f'Final N = {n}')
        return n