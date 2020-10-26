

class Solution: 

    def foursum(self, n, target):

        result, result_set = [], set()
        n.sort()

        for i in range(len(n) - 1):

            if i > 0 and n[i] == n[i-1]:
                continue
            for j in range(i+1, len(n)):

                l, r = j+1,len(n)-1

                while l < r:
                    x = n[i] + n[j] + n[l] + n[r]

                    if x < target:
                        l +=1
                    elif x > target:
                        r -=1

                    elif (n[i], n[j], n[l], n[r]) not in result_set:

                        result.append([n[i], n[j], n[l], n[r]])
                        result_set.add((n[i], n[j], n[l], n[r]))

                    else:
                        l, r = l+1, r-1

        return result

if __name__ == '__main__':

    n, target = [1, 0, -1, 0, -2, 2], 0
    Solution().foursum(n, target)

