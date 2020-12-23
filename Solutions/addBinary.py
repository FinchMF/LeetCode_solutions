
class Solution:

    def addBinary(self, a: str, b: str) -> str:

        return str(bin(int(a,2) + int(b,2)))[2:]


if __name__ == '__main__':

    a, b = "11", "1"
    print(Solution().addBinary(a,b))