"""
Given a cost matrix cost[][] and a position (m, n) in cost[][], create a function that 
returns cost of minimum cost path to reach (m, n) from (0, 0)
"""

def get_min(cost, m, n):
    #base condtions
    if m == 0 and n == 0:
        return cost[0][0]

    if m == 0:
        return get_min(cost, m, n-1) + cost[0][n]

    if n == 0 :
        return get_min(cost, m-1, n) + cost[m][0]
    
    #recursions calls
    a = get_min(cost, m-1, n)
    b = get_min(cost, m, n-1)

    #getting min
    return min(a, b) + cost[m][n]    

# driver code
cost_matrix = [[1,2,3,4], [5,6,7,8], [9,1,2,5]]
print(get_min(cost_matrix, 1, 2))    