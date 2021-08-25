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

# to avoid the issue with different lenght of lists

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
Create a function to remove duplicates from the list
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
Create a function to find index of min/max element in the list
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

"""
Create a decorator
"""

def some_decorator(f):
    def wraps(*args):
        print(f"Calling function '{f.__name__}'")
        return f(args)
    return wraps

@some_decorator
def decorated_function(x):
    print(f"With argument '{x}'")

print(decorated_function("python"))    

"""
Create a function to take limited history of the last few items seen during iteration or streem processing
"""

from collections import deque

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

with open("./words.txt") as f:
	for line, prevlines in search(f, 'across', 5):
		for pline in prevlines:
			print(pline, end='')
		print(line, end='')
		print('-'*20)

"""
Create priority queue
"""

import heapq

# function to find N max or min elements of sequence
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))

portfolio = [
   {'name': 'IBM', 'shares': 100, 'price': 91.1},
   {'name': 'AAPL', 'shares': 50, 'price': 543.22},
   {'name': 'FB', 'shares': 200, 'price': 21.09},
   {'name': 'CSCO', 'shares': 35, 'price': 31.75},
   {'name': 'YHOO', 'shares': 45, 'price': 16.35},
   {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['shares'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])

# Item and PQ classes
class Item:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Item({!r})'.format(self.name)

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

q = PriorityQueue()
for idx, val in enumerate(nums):
    print(idx, val)
    q.push(Item(val), idx)
print(q.pop())

"""
Create a function to map multiple values to key in dictionary
"""

from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

d1 = defaultdict(set)
d1['a'].add(1)
d1['a'].add(2)
d1['b'].add(4)

print(d, d1)

"""
Create function to compare and sort dictionaries
"""

import collections

a = {'x' : 1, 'y' : 2, 'z' : 3}
b = {'w' : 10, 'x' : 11,'y' : 2}

# Find keys in common
print(a.keys() & b.keys())

# Find keys in a that are not in b
print(a.keys() - b.keys())

# Find (key,value) pairs in common
print(a.items() & b.items())

# Sorting dictionaries
prices = {'apple': 4.23,'orange': 12.78,'bananas': 0.55,'avocado': 7.20,'strawberry': 20.75}
min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
print(min_price)
print(max_price)

# Sorintg using collections Counter
sorted_di_coll = collections.Counter(prices)
print(f"sorted with collection.Counters() {sorted_di_coll.most_common(len(prices.keys()))}")

# Sorting using sorted() functions
sorted_di = sorted(prices.items(), key=lambda x: x[1], reverse=True)
print(f"sorted with sorted function and key option {sorted_di}")

"""
Create a function to count groups and elements in groups in sequence
"""

import itertools  
 
arr = "AAAABBBCCDAABDAAAAC"
print([list(g) for k, g in itertools.groupby(arr)])
print([k for k, g in itertools.groupby(arr)])
for item in [list(g) for k, g in itertools.groupby(arr)]:
    print(len(item),item[0])

"""
Create a class to simulate dice throwing game
"""

import random

class MSD:
    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.current_value = self.roll()

    def roll(self):
        self.current_value = random.randrange(1,self.num_sides)
        return self.current_value

    def __str__(self):
        return str(self.current_value)

    def __repr__(self):
        return "MSD({}) : {}".format(self.num_sides, self.current_value)

my_dice = MSD(6)
for i in range(5):
    print(my_dice)
    my_dice.roll()

d_list = [MSD(6), MSD(20)]
print(d_list)

"""
Heapify function from "Inroduction to Algorithm" books
"""

def left(i):
    return 2*i

def right(i):
    return 2*i +1

def parent(i):
    return i/2

def heapify(arr, i):
    l = left(i)
    r  = right(i) 
    if l <= len(arr)-1 and arr[l] > arr[i]:
        largest = l
    else:
        largest = i
    if r <= len(arr)-1 and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, largest)

    return arr

arr = [-4, 2, 1, 23, 7, 2, 18, 23, 42, 37, 8]
for i in range(len(arr)//2, -1, -1):
    heapify(arr, i)

print(arr)

"""
Class and closure comparison
"""

class NthRoot:
    def __init__(self, n=2):
        self.n = n
    
    def set_root(self,n):
        self.n = n
    
    def calc(self, x):
        return x ** (1/self.n)

def nth_root(n=2):
    def calc(x):
        return x ** (1/n)
    return calc

thirdRoot = NthRoot(3)
print("Class example ", thirdRoot.calc(27))

third_root = nth_root(3)
print("Closure example ", third_root(27))