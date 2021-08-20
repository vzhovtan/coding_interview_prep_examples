"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
"""

class Solution():
    def __init__(self, s, p):
        self.orig = s
        self.template = "".join(sorted(p))
        print(self.template)

    def find_index(self):
        self.limit = len(self.template)
        print(self.limit)
        self.finish = len(self.orig) - self.limit
        print(len(self.orig))
        print(self.finish)

        for i in range(0, self.finish+1):
            print("curent i", i)
            self.current = "".join(sorted(self.orig[i:i+self.limit]))
            if self.template == self.current:
                print(self.current)
                print(i)
                    
# driver code
s = "cbaebabacd"
p = "abc"
sol = Solution(s,p)
sol.find_index()