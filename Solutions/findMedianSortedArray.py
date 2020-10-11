

class Solution:
    
        def findMedianSortedArrays(self, arr_1, arr_2):
            # set the array
            array = sorted(arr_1 + arr_2)
            print(f'Combined Array, Sorted: \n {array} \n ')
            print('Is array length even or odd? \n')
             # if the array's length is even
            if len(array) % 2 == 0: 
                print(f'Even -- Number of Elements: {len(array)}')
                return (array[len(array) // 2] + array[len(array) // 2 + 1]) / 2
        
            # if the array's length is odd
            else: 
                print(f'Odd -- Number of Elements: {len(array)} \n')
                return array[len(array) // 2]
