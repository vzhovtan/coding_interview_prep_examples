"""
Given two strings S and T, determine if they are both one edit distance apart.
I.e. different by one character
- If | n – m | is greater than 1, we know immediately both are not one-edit distance apart.

We make a first pass over S and T concurrently and stop at the first non-matching 
character between S and T.
1. If S matches all characters in T, then check if there is an extra character at the end of T. (Modify operation)
2. If | n – m | == 1, that means we must skip this non-matching character only in T 
and make sure the remaining characters between S and T are exactly matching. (Insert operation)
3. If | n – m | == 0, then we skip both non-matching characters in S and T 
and make sure the remaining characters between S and T are exactly matching. (Append operation)

Returns true if edit distance between s1 and s2 is one, else false
"""

def isEditDistanceOne(s1, s2):
    lens1 = len(s1)
    lens2 = len(s2)
 
    # If difference between lengths is more than 1, then strings can't be at one distance
    if abs(lens1 - lens2) > 1:
        return False
 
    count = 0
    i, j = 0, 0
    while i < lens1 and j < lens2:
        if s1[i] != s2[j]:
            if count == 1:
                return False
            # If length of one string is more, then only possible edit is to remove a character
            if lens1 > lens2:
                i+=1
            elif lens1 < lens2:
                j+=1
            else:    # If lengths of both strings is same
                i+=1
                j+=1
            count += 1
 
        else:    # if current characters match
            i+=1
            j+=1
 
    # if last character is extra in any string
    if i < lens1 or j < lens2:
        count+=1
 
    return count == 1
 
# driver code
s1 = "gfg"
s2 = "gf"
if isEditDistanceOne(s1, s2):
    print("Yes")
else:
    print("No")