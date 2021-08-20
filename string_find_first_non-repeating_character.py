"""
Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. 
If there is no such character, return '_'.

Example
For s = "abacabad", the output should be
firstNotRepeatingCharacter(s) = 'c'.

There are 2 non-repeating characters in the string: 'c' and 'd'. 
Return c since it appears in the string first.

For s = "abacabaabacaba", the output should be
firstNotRepeatingCharacter(s) = '_'.

There are no characters in this string that do not repeat.
"""

def firstNotRepeatingCharacter(s):
    count = {}

    for i in range(len(s)):
        if s[i] in count.keys():
            count[s[i]] += 1
        else:
            count[s[i]] = 1

    for k, v in count.items():
        if v == 1:
            return k

    return "_"

# driver code
print(firstNotRepeatingCharacter("abacabad"))
print(firstNotRepeatingCharacter("aa"))
print(firstNotRepeatingCharacter(""))


    