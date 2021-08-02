"""
Dutch flag problem
Given an array A[] consisting 0s, 1s and 2s. 
The task is to write a function that sorts the given array. The functions should put all 0s first, then all 1s and all 2s in last.
"""

import random

def partition_inplace_with_additional_memory(A, start, stop, pivot_value):
    items_less_than = []
    items_greater_than_or_equal = []
    
    read_index = start
    while read_index <= stop:
        item = A[read_index]
        if item < pivot_value:
            items_less_than.append(item)
        else:
            items_greater_than_or_equal.append(item)
        read_index += 1
    
    return items_less_than, items_greater_than_or_equal    

def partition_inplace_value(A, start, stop, pivot_value):
    curr_index = start
    while curr_index <= stop:
        item = A[curr_index]
        # if the current item is less than the pivot value
        if item < pivot_value:
            # swap it at the insertion position
            A[start], A[curr_index] = A[curr_index], A[start]
            # and move the insertion position one up
            start += 1
        curr_index += 1

def dutch_flag (arr, pivot):
    smaller, equal, larger = 0, 0, len(arr) 
    while equal < larger:
        if arr[equal] < pivot:
            arr[smaller], arr[equal] = arr[equal], arr[smaller]
            smaller, equal = smaller + 1, equal+ 1
        
        elif arr[equal] == pivot:
            equal += 1
        
        else: #arr[equal] > pivot
            larger -= 1
            arr[equal], arr[larger] = arr[larger], arr[equal]     

# driver code
A = [random.randrange(10) for i in range(10)]
less, greater = partition_inplace_with_additional_memory(A, 0, len(A)-1, 5)
print(f"partition_inplace_with_additional_memory, less is {less} \n")
print(f"partition_inplace_with_additional_memory, greater is {greater} \n")

partition_inplace_value(A, 0, len(A)-1, 5)
print(f"A partitioned inplace is {A} \n")

dutch_flag (A, 5)
print(f"A after applying dutch flag algo {A} \n")