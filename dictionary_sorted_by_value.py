"""
Couple of example how to sort Python dictionary by value
"""

import collections

di  = { 'cappuccino': 54,
        'latte': 56,
        'espresso': 72,
        'americano': 48}

# using collections Counter
sorted_di_coll = collections.Counter(di)
print(f"sorted with collection.Counters() {sorted_di_coll.most_common(len(di.keys()))}")

# using sorted() functions
sorted_di = sorted(di.items(), key=lambda x: x[1], reverse=True)
print(f"sorted with sorted function and key option {sorted_di}")
