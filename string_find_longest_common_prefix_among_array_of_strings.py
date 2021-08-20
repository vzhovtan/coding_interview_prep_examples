"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
"""

def longestCommonPrefix(strs):
    if not strs:
        return ""

    shortest = min(strs,key=len)
    # print(shortest)
    for i, char in enumerate(shortest):
        for other in strs:
            if other[i] != char:
                return shortest[:i]

    return shortest 

# driver code
print(longestCommonPrefix(["flower","flow","flight"])) #"fl"
print(longestCommonPrefix(["dog","racecar","car"])) # ""