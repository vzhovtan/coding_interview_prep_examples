"""
Find the mango seller in your social network. Social network represented as graph and mango seller could be identified as person with the name
ended with letter 'm'
The example is take from the book 'Grokking algorithms' and used with some modification in 'breadth-first_search_with_route_2' example to find
not only the person but identify the shortest path toeards the person over social network connections
"""

from collections import deque

def person_is_seller(name):
    # define is a person is mango seller if his/her name end with letter m
    return name[-1] == 'm'

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    # This is how you keep track of which people you've searched before.
    searched = set()
    while search_queue:
        person = search_queue.popleft()
        # Only search this person if you haven't already searched them.
        if person not in searched:
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                # Marks this person as searched
                searched.add(person)
    return False

# driver code
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["tom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["tom"] = []
graph["jonny"] = []

search("you")
