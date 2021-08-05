"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.
Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a <= b <= c)
The solution set must not contain duplicate triplets.
For example, given array S = {-1 0 1 2 -1 -4},
   A solution set is:
   (-1, 0, 1)
   (-1, -1, 2)
"""

import collections

class Solution(object):
    def threeSum(self, arr):
        res =[]
        d = collections.Counter(arr) # count all appareance in the input list as counter object
        if d[0] >= 3:
            res = [[0,0,0]] # edge case when 3 zeroes are in the input list
        done = {}
        for n, i in enumerate(arr):
            for k, j in enumerate(arr[n+1:]):
                if 0-i-j in arr[k+1:] and 0-i-j not in done.keys(): #looping over list elements and checking if (0 - 2 elements) in hash to avoid looping 3rd time 
                    if sorted([i, j, 0-i-j]) not in res:
                        res.append(sorted([i, j, 0-i-j]))
                    done[0-i-j] = 1 
        return res

    def find_triplet(self, arr):
        unique_lists = []
        num_list = []

        if len(arr) >= 3: 
            for i in range(len(arr)):
                for j in range(i+1, len(arr)):
                    for g in range(i+2, len(arr)):
                        if arr[i] + arr[j] + arr[g] == 0:
                            num_list.append(arr[i])
                            num_list.append(arr[j])
                            num_list.append(arr[g])
                            num_list.sort()

                            if num_list not in unique_lists:
                                unique_lists.append(num_list)
                            num_list = []
            if unique_lists == []:
                return None

            return unique_lists
        else:
            return None    

# driver code
result1 = Solution().threeSum([-1, 0, 1, 2, 2, -1, -4, -4, 0, 0])
result2 = Solution().find_triplet([-1, 0, 1, 2, 2, -1, -4, -4, 0, 0])
print(result1)
print(result2)