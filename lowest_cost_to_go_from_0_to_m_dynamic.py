"""
Given a cost matrix cost[][] and a position (m, n) in cost[][], create a function that 
returns cost of minimum cost path to reach (m, n) from (0, 0)
"""

def find_min_cost_dp(cost, d):
    min_cost = [0 for x in range(len(cost))]
    print("first time ", min_cost)
    min_cost[0] = 0
    min_cost[1] = cost[0][1]
    print("after adding 0 and 1 ", min_cost)

    for i in range(2,len(cost)):
        min_cost[i] = cost[0][i]
        print("i is ", i, "min cost is ", min_cost)
        for j in range(i):
            print("min_cost[j] ",  min_cost[j], " cost[j][i] ", cost[j][i])
            if min_cost[i] > min_cost[j] + cost[j][i]:
                min_cost[i] = min_cost[j] + cost[j][i]
    print(min_cost)
    return min_cost[d]

# driver code
cost_i_to_j = [[ 0, 10, 75, 94],
            [-1, 0, 35, 40],
            [-1, -1, 0, 4],
            [-1, -1, -1, 0]]
print(find_min_cost_dp(cost_i_to_j, 3))