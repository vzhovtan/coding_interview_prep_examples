"""
Create a function to concatenate following dictionaries to create a new one. Go to the editor

Sample Dictionary : 
dic1={1:10, 2:20} 
dic2={3:30, 4:40} 
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
""" 

def concatenate(dict1, dict2, dict3):
	new_dict = {}
	for value in (dict1, dict2, dict3):
		new_dict.update(value)
	return new_dict

print(concatenate({1:10, 2:20}, {3:30, 4:40}, {5:50,6:60}))

"""
Create a function to check if a given key already exists in a dictionary.
"""

def find_key(dictionary, key):
	if dictionary.get(key):
		return True
	else:
		return False

print(find_key({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}, 3))
print(find_key({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}, 9))

"""
Create a function to iterate over dictionaries using for loops.
"""

def iterate_dictionary(dictionary):
	for i in dictionary:
		print(i, dictionary[i])

iterate_dictionary({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60})

""" 
Create a function to generate and print a dictionary that contains a number (between 1 and n) 
in the form (x, x*x).
Sample Dictionary (n = 5): 
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""

def generate_dict(num):
	new_dict = {}
	for i in range(1, num + 1):
		new_dict[i] = i * i
	return new_dict

print(generate_dict(5))
print({n: n*n for n in range(1, 6)}) # better

"""
Create a function to map two lists into a dictionary.
"""

def zip_lists(keys, values):
	return dict(zip(keys, values))

print(zip_lists([1, 2, 3, 4, 5], ["a", "b", "c", "d", "e"]))

"""
Create a function to count occurrences in the given list
"""

from collections import Counter

num_lst = [1, 1, 2, 3, 4, 5, 3, 2, 3, 4, 2, 1, 2, 3]
cnt = Counter(num_lst)
# first 2 most occurrence
print(dict(cnt.most_common(2)))

"""
Create a function to check if all chars are upper case in given string
"""

import string

def is_upper(word):
    return all(c in string.ascii_uppercase for c in list(word))

print(is_upper("ABRACADABRA"))
print(is_upper("abracadabra"))

"""
Create a function to transpose 2D array
"""
from itertools import zip_longest

inpt = [['a', 'b'], ['c', 'd'], ['e', 'f']]
transposed = zip(*inpt)
print(list(transposed))

inpt = [['a', 'b'], ['c', 'd'], ['e', 'f', 'g', 'h']]
transposed = zip_longest(*inpt)
print(list(transposed))

"""
Create a function to loop over multiple lists at the same time
"""

colors = ["red", "green", "yellow", "blue"]
codes = [1, 2, 3, 4]
for color, code in zip(colors, codes):
    print(f"{code}, {color}")

from itertools import zip_longest

colors = ["red", "green", "yellow", "blue"]
codes = [1, 2, 3, 4, 5, 6]
for color, code in zip_longest(colors, codes):
    print(f"{code}, {color}")

for color, code in zip_longest(colors, codes, fillvalue='Nothing'):
    print(f"{code}, {color}")

"""
Create a function to return an iterator that returns the results of a function
"""
import itertools
import operator

data = [1, 2, 3, 4, 5]
result = list(itertools.accumulate(data, operator.add))
print(result)

"""
Create a function to reverse list or string
"""

a = "whatsup"
print(f"Reversed : {a[::-1]}")

b = [1, 2, 3, 4, 5]
print(f"Reversed : {b[::-1]}")

"""
Create a function to join string and list together
"""

str1 = "have"
str2 = "fun"
lst = ["Don't", "worry"]

str3 = ' '.join(lst) + ', ' + str1 + ' ' + str2
print(str3)

"""
Create a function to convert list to comma separated string
"""

fruits = ['apple', 'mango', 'orange']
print(', '.join(fruits))

numbers = [1, 2, 3, 4, 5]
print(', '.join(map(str, numbers)))

items = [1, 'apple', 2, 3, 'orange']
print(', '.join(map(str, items)))

"""
Create a function to flatten nested list
"""

import itertools

flatten = lambda x: list(itertools.chain.from_iterable(x))
s = [['Every', 'piece of'], ['software written today is', 'likely'], ['going to'], 
['infringe on', "someone else’s", 'patent.']]
print(' '.join(flatten(s)))

"""
Create a function to call different functions with the same arguments based on conditions
"""

def product(a, b):
    return a*b

def add(a, b):
    return a+b

# c = True
c = False
print((product if c else add)(5, 6))

"""
Create a function to sort dictionary
"""

from operator import itemgetter

d = {'a': 10, 'b': 20, 'c': 5, 'd': 8, 'e': 5}
# sort by value
print(sorted(d.items(), key=lambda x: x[1]))
# sort by value
print(sorted(d.items(), key=itemgetter(1)))
# sort by key
print(sorted(d.items(), key=itemgetter(0)))
# sort by value and return keys
print(sorted(d, key=d.get))

"""
Cretae a function to remove duplicates from the list
"""

lst = [7, 3, 3, 5, 6, 5]

# removes duplicates but does not preserves the list order
no_dups = list(set(lst))
print(no_dups)

# removes duplicates and preserves the list order
from collections import OrderedDict
no_dups = list(OrderedDict.fromkeys(lst).keys())
print(no_dups)

"""
Create a fucntion to find index of min/max element in the list
"""

def min_idx(lst):
    return min(range(len(lst)), key=lst.__getitem__)


def max_idx(lst):
    return max(range(len(lst)), key=lst.__getitem__)


lst = [20, 40, 70, 10]
print("min idx : {}".format(min_idx(lst)))
print("max idx : {}".format(max_idx(lst)))

"""
Create a function to check if the given string is anagramm
"""

from collections import Counter

print(Counter("abbada") == Counter("adabba"))
print(Counter("yes") == Counter("not"))


