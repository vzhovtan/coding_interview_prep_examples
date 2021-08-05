"""
Given an array of integers, find two numbers such that they add up to a specific target number.
"""

def two_sum_brute(arr, target):
    """
    brute-force aproach
    """
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == target:
                print(f"Brute force values are {arr[i]} and {arr[j]}")

def two_sum_hash(arr, target):
    """
    hash table approach
    """
    hashtable = {}
    for i in range(len(arr)):
        second = target - arr[i]
        if second in hashtable.keys():
            print (f"Hash table values are {second} and {arr[i]}")
            # print(hashtable)
        hashtable[arr[i]] = i 

def two_sum_sorted_two_pointers(arr, target):
    i, j = 0, len(arr) -1
    while i < j:
        summ = arr[i] + arr [j]
        if summ < target:
            i += 1
        elif summ > target:
            j -= 1
        else:
            print (f"Sorted with two pointers values are {arr[i]} and {arr[j]}")
            i += 1

# driver code
arr = [x for x in range(10)]
k = 12
print(f"array is {arr}, target is {k}")
two_sum_brute(arr, k)
two_sum_hash(arr, k)
two_sum_sorted_two_pointers(arr, k)