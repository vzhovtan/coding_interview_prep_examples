"""
Find the shortest path from the start to the destination in given graph represented as dictionary of lists
"""

def BFS_SP(graph, start, goal):
    explored = []
    # Queue for traversing the graph in the BFS
    queue = [[start]]
     
    # If the desired node is reached
    if start == goal:
        print("Same Node")
        return
     
    # Loop to traverse the graph with the help of the queue
    while queue:
        print("queue", queue)
        path = queue.pop(0)
        print("path", path)
        node = path[-1]
        print("node", node)
         
        # Condition to check if the current node is not visited
        if node not in explored:
            neighbours = graph[node]
            print("neighbours", neighbours)
             
            # Loop to iterate over the neighbours of the node
            for neighbour in neighbours:
                new_path = list(path)
                print("new_path", new_path)
                new_path.append(neighbour)
                queue.append(new_path)
                 
                # Condition to check if the neighbour node is the goal
                if neighbour == goal:
                    print("Shortest path = ", *new_path)
                    return
            explored.append(node)
 
    # Condition when the nodes are not connected
    print("Connecting path doesn't exist")
    return
 
# driver code
graph = {'A': ['B', 'E', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F', 'G'],
        'D': ['B', 'E'],
        'E': ['A', 'B', 'D'],
        'F': ['C'],
        'G': ['C']}
     
BFS_SP(graph, 'A', 'D')