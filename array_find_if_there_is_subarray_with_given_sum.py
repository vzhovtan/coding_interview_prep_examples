"""
Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum. 
"""

def isSubsetSum(set, n, sum):
    # Base Cases
    if (sum == 0):
        return True
    if (n == 0):
        return False
 
    # If last element is greater than sum, then ignore it
    if (set[n - 1] > sum):
        return isSubsetSum(set, n - 1, sum)
 
    #else, check if sum can be obtained by any of the following
    # (a) including the last element
    # (b) excluding the last element
    return isSubsetSum(set, n-1, sum) or isSubsetSum(set, n-1, sum-set[n-1])
 
# driver code
set = [3, 34, 4, 12, 5, 2]
sum = 9
n = len(set)
if (isSubsetSum(set, n, sum)):
    print("Found a subset with given sum")
else:
    print("No subset with given sum")
 