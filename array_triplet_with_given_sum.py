"""
Given an array A[] of N numbers and another number x, determine 
whether or not there exist three elements in A[] whose sum is exactly x.
"""

def find_triplet(array, n, x):
    for i in range(n-1):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                print(array[i], array[j], array[k])
                if (array[i] + array[j] + array[k]) == x:
                     return 1                    

# driver code
arr = [1, 4, 45, 6, 10, 8]
n = len(arr)
x = 11
print(find_triplet(arr, n, x)) 