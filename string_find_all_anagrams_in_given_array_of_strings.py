"""
Find all anagrams in a given array of strings reperesented as string 
The string "eat tea tan ate nat bat" is actually and array ["eat", "tea", "tan", "ate", "nat", "bat"] and produce
-ate eat tea
-bat
-nat tan
"""

from collections import defaultdict

def get_anagrams(source):
    d = defaultdict(list)
    for word in source:
        print(word)
        key = "".join(sorted(word))
        #or
        #key = str(sorted(word)) # the result is the same key has not meaning in this case just to be hashable
        print(key)
        d[key].append(word)
        print(d)
    return d

def print_anagrams(my_string):
    word_source = my_string.split(" ")
    d = get_anagrams(word_source)
    for _, anagrams in d.items():
        print(" ".join(sorted(anagrams)))

print_anagrams("eat tea tan ate nat bat")