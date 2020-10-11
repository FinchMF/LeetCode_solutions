

class Solution:

    def intToRoman(self, n: int) -> str:

        r_num = "M" * (n // 1000)
        r_num += "CM" if n % 1000 >= 900 else "D" *((n % 1000) // 500)
        r_num += "CD" if n % 500 >= 400 and r_num[-2:] != "CM" else "C" * ((n % 500) // 100)  if n % 500 < 400 else ""
        r_num += "XC" if n % 100 >= 90 else "L" * ((n % 100) // 50)
        r_num += "XL" if n % 50 >= 40 and r_num[-2:] != "XC" else "X" * ((n % 50) // 10)  if n % 50 < 40 else ""
        r_num += "IX" if n % 10 >= 9 else "V" * ((n % 10) // 5)
        r_num += "IV" if n % 5 >= 4 and r_num[-2:] != "IX" else "I" * ((n % 5) // 1) if n % 5 < 4 else ""
        
        return r_num