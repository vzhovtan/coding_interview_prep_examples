"""
Given an array of integers, every element appears three times except for one. Find that single one.
Note:
Your algorithm should have a linear runtime complexity.
"""

import collections

class Solution1(object):
    def singleNumber(self, A):
        one, two, carry = 0, 0, 0
        for x in A:
            two |= one & x
            one ^= x
            carry = one & two
            one &= ~carry
            two &= ~carry
        return one

class Solution2(object): #best one
    def singleNumber(self, nums):
        return (sum(set(nums)) * 3 - sum(nums)) / 2

# driver code
print(Solution1().singleNumber([1, 1, 1, 2, 2, 2, 3]))
print(Solution2().singleNumber([1, 1, 1, 2, 2, 2, 3]))
