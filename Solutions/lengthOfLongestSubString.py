

class Solution:

    def lengthOfLongestSubstring(self, s):

        substring_len = 0 
        count = 0
        chars_counter = {}

        print(f'Substring Length: {substring_len}', end='\n * ')
        print(f'Count: {count}', end='\n * ')
        print('[+] Character counter Set')
        print('\n')

        for idx in range(len(s)):
            print(f' [i] currently at index: {idx}')
            if s[idx] in chars_counter and count <= chars_counter[s[idx]]: 
                print(f'[---] Current Element: {s[idx]}')
                print(f'[---] Count at: {count}')
                print('\n')
                count = chars_counter[s[idx]] + 1
                print('[i] Charater Counted \n')
            else: 
                print(f'[---] Current Element: {s[idx]}')
                print(f'[---] Substring Length at: {substring_len}')
                print('\n')
                substring_len = max(substring_len, idx - count + 1)
            chars_counter[s[idx]] = idx
            print(f'Current Counts: {chars_counter}')
            print('\n')

        return substring_len