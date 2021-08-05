"""
Given 3 lists A, B, C of integer values, compute how many tuples (i, j, k) there are
such that A[i] + B[j] + C[k] is zero.
To make problem a bit easier, all A, B, C have same length of N where 0 <= N <= 500.
All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.
"""

import collections

class Solution(object):
    def threeSumCount(self, A, B, C):
        """
        The idea is to count how many combinations of a+b is there and then compare if the combination's key == -c
        which is equal to a+b+c == 0
        """
        A_B_sum = collections.Counter(a+b for a in A for b in B)
        print("first_Counter", A_B_sum)
        for item in (A_B_sum[c] for c in C):
            print("Taking the item equal to a+b=-c, which is the same as a+b+c=0", item)
        return sum(A_B_sum[-c] for c in C)

# driver code
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
sol = Solution()
print(sol.threeSumCount(A, B, C))