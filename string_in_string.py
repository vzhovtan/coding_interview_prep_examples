"""
Implement strstr().Returns the index of the first occurrence of needle in haystack, or –1
if needle is not part of haystac
"""

def strstr1(needle, haystack): # Return True or False
    n = len(needle)
    for i in range(len(haystack)-1):
        # Check if the substring (i:i+n) at this position matches haystack
        if haystack[i:i+n] == needle:
            # If there is a match, we're done
            return True
    #otherwise return -1 indicateing failure
    return False

def strstr2(sub, full): # Return starting index of substring
    for i in range(len(full)-len(sub)+1):
        for j in range(len(sub)):
            # print("i", i, "j", j)
            # print("sub", sub[j], "full", full[i+j])
            if sub[j] != full[i+j]:
                break
            elif j == len(sub)-1:
                return i   

# driver code
needle = "abc"
hay = "abcfrsfabc"
print(strstr1(needle, hay))
print(strstr2(needle, hay))