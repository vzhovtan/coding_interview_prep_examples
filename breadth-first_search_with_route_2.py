"""
Find the shortest path from the start to the destination in given graph represented as dictionary of lists
"""

import copy 

def find_route(start, end):
    done = set()
    neig = []
    for item in graph[start]:
        route = [start, item]
        neig.append(route)
    
    print("start neig", neig)   #[['cab', 'cat'], ['cab', 'car']]

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
# driver code
graph = {}
graph["cab"] = ["cat", "car"]
graph["cat"] = ["mat", "bat"]
graph["car"] = ["cat", "bar"]
graph["bar"] = ["bat"]
graph["mat"] = ["bat"]
graph["bat"] = ["blah"]

find_route("cab", "blah")