"""
Given a cost matrix cost[][] and a position (m, n) in cost[][], create a function that 
returns cost of minimum cost path to reach (m, n) from (0, 0)
"""

def get_min(cost, m, n):
    memo = [[0 for x in range(n+1)] for x in range(m+1)]
    if memo[m][n] != 0:
        return memo[m][n]
    #base condtions
    if m == 0 and n == 0:
         memo[0][0] = cost[0][0]

    elif m == 0:
        memo[m][n] = get_min(cost, m, n-1) + cost[0][n]

    elif n == 0 :
        memo[m][n] = get_min(cost, m-1, n) + cost[m][0]
    
    else:
        a = get_min(cost, m-1, n)
        b = get_min(cost, m, n-1)
        #getting min
        memo[m][n] = min(a, b) + cost[m][n]

    return memo[m][n]        

# driver code
cost_matrix = [[1,2,3,4], [5,6,7,8], [9,1,2,5]]
print(get_min(cost_matrix, 1, 2))    