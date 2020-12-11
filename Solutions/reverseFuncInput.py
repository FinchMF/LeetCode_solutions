
class Solution:

    def reverseFuncInput(self, f):

        return lambda *args: f(*args[::-1])


if __name__ == '__main__':

    x, y = 4, 5

    def func(x,y):
        return x**y

    g=Solution().reverseFuncInput(func)

    print(func(x,y))
    print(g(x,y))





    



