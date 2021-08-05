"""
Given an array arr[]. Find the maximum for each and every non-contiguous subarray.

A naive solution to this problem is to calculate the sum of all possible subsequences with no adjacent elements 
and keep track of the subsequence with the maximum sum. 
The time complexity of this approach is O(n2)O(n^2)O(n​2​​).

This can be improved by using dynamic programming. Iterate over the entire input array, and in every iteration pick the maximum of these two values:
--Max Sum of the last iteration.
--Max Sum of second last iteration + current iteration index.
"""

def find_max_sum_nonadjacent(a):
  if len(a) < 1:
    return 0
  elif(len(a) == 1):
    return a[0]

  lengthA = len(a)
  result = []
  result.append(a[0])
  
  for i in range(1, lengthA):
    result.append(max(a[i], result[i - 1]))
    if i - 2 >= 0 :
      result[i] = max(result[i], a[i] + result[i - 2])
    
  return result[lengthA - 1]

# driver code
v = [1, -1, 6, -4, 2, 2]
sum = find_max_sum_nonadjacent(v)
print("Max sum of nonadjacent subsequence: " + str(sum))