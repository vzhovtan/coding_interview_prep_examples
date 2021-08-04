"""
Given an array strings, determine whether it follows the sequence given in the  patterns array. In other words, there should be no i and j 
for which 
strings[i] = strings[j] and patterns[i] ≠ patterns[j] 
or for which 
strings[i] ≠ strings[j] and patterns[i] = patterns[j].

Example:
For strings = ["cat", "dog", "dog"] and patterns = ["a", "b", "b"], 
the output should be areFollowingPatterns(strings, patterns) = true;
For strings = ["cat", "dog", "doggy"] and patterns = ["a", "b", "b"], the 
output should be areFollowingPatterns(strings, patterns) = false.
"""

def areFollowingPatterns(strings, patterns):
    if len(strings) != len(patterns):
        return False
    s_dict = {}
    p_set = set()
    s_set = set()
    
    for i in range(len(patterns)):
        p_set.add(patterns[i])
        s_set.add(strings[i])

        if patterns[i] not in s_dict.keys():
            s_dict[patterns[i]] = []

        keys = s_dict[patterns[i]]
        keys.append(strings[i])
        s_dict[patterns[i]] = keys
        print("pset", p_set, "sset", s_set, "sdict", s_dict)

    if len(p_set) != len(s_set):
        return False   

    for values in s_dict.values():
        for i in range(len(values) - 1):
            if values[i] != values[i+1]:
                return False
    
    return True

# driver code
print(areFollowingPatterns(["cat", "dog", "doggy"], ["a", "b", "b"])) 
# expected False

print(areFollowingPatterns(["cat", "dog", "cat", "dog"], ["a", "b", "a", "b"])) 
# expected True
