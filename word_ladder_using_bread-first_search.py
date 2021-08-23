"""
Used regular dictionary file to select words with 4 letters only and create a function to build word ladder 
from given start to end using bread first search algoritm
"""

import copy

d = {}
graph = {}

with open("./words.txt") as fd:
    for line in fd.readlines():
        word = line.rstrip("\n")
        if len(word) == 4:
            for i in range(len(word)):
                bucket = word[:i] + '_' + word[i+1:]
                if bucket in d.keys():
                    d[bucket].append(word)
                else:
                    d[bucket] = [word]

# for key, value in d.items():
#     if len(value) > 2:
#         print(key, value)

for bucket in d.keys():
    for item1 in d[bucket]:
        for item2 in d[bucket]:
            if item1 in graph.keys() and item2 != item1:
                graph[item1].append(item2)
            else:
                graph[item1] = [item2]

# for key, value in graph.items():
#     if len(value) > 3:
#         print(key, value)

def find_route(start, end):
    done = set()
    neig = []
    for item in graph[start]:
        route = [start, item]
        neig.append(route)
    
    print("start neig", neig)

    while neig:
        item = neig.pop(0)
        print("current item", item)
        node = item[-1]
        print("current node", node)
        if node not in done:
            for nextnode in graph[node]:
                print("nextnode", nextnode)
                print("item", item)
                new_route = copy.deepcopy(item)
                new_route.append(nextnode)
                print("new route", new_route)
                if nextnode == end:
                    print ("found the route", new_route)
                    return True    
                else:
                    neig.append(new_route)
                    done.add(node)    
                    print("currrent neig", neig)
                    print("current done", done)
    return False                

find_route("scud", "shun")