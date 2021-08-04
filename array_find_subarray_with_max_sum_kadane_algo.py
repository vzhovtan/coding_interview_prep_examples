"""
Write an efficient program to find the sum of contiguous subarray within a one-dimensional array of numbers which has the largest sum.
he basic idea of Kadane’s algorithm is to scan the entire array and at each position find the maximum sum of the subarray ending there. 
This is achieved by keeping a current_max for the current array index and a global_max.

Kadane's algo
Initialize:
    max_so_far = 0
    max_ending_here = 0

Loop for each element of the array
  (a) max_ending_here = max_ending_here + a[i]
  (b) if(max_so_far < max_ending_here)
            max_so_far = max_ending_here
  (c) if(max_ending_here < 0)
            max_ending_here = 0
return max_so_far
"""

def find_sub_max(arr):
    max_so_far =0
    max_end_here = 0
    for item in arr:
        max_end_here += item
        if max_so_far < max_end_here:
            max_so_far = max_end_here
        if max_end_here < 0:
            max_end_here =0
    
    return max_so_far            

def find_max_sum_sub_array(A):
  if len(A) < 1:
    return 0

  curr_max = A[0]
  global_max = A[0]
  lengthA = len(A)
  for i in range(1, lengthA):
    if curr_max < 0:
      curr_max = A[i]
    else:
      curr_max += A[i]

    if global_max < curr_max:
      global_max = curr_max

  return global_max

# driver code
array = [-2, -3, 4, -1, -2, 1, 5, -3]
print(find_sub_max(array))  
print(find_max_sum_sub_array(array))
