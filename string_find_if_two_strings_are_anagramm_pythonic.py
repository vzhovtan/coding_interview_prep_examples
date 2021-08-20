"""
Create a function to find if two strings are anagramm
"""

import collections

class Solution1:
    # Converting strings to lists and sorting them for furhter comparison
    def __init__(self, str1, str2):
        self.alist1 = list(str1)
        self.alist2 = list(str2)
        self.alist1.sort()
        self.alist2.sort()

    def compare(self):
        if len(self.alist1) != len(self.alist2):
            print("Lenght of thwo string is different")
            return False
        else:
            matches = True
            for n, let in enumerate(self.alist1):
                if let != self.alist2[n]:
                    matches = False
        return matches

class Solution2():
    # Counter for each letter, if amount of the same letters is the same in both strings they are anagramm
    def __init__(self, str1, str2):
        self.count1 = collections.Counter(str1)
        self.count2 = collections.Counter(str2)
    
    def compare (self):
        for key, val in self.count1.items():
            if val != self.count2[key]:
                return False

        return True

# driver code
str1 = "apple"
str2 = "pleap"

sol1 = Solution1(str1, str2)
print(sol1.compare())

sol2 = Solution2(str1, str2)
print(sol2.compare())


