"""
Find equilibrium index in a given array. If it does not exist, return 1.
"""

def find_equilibrium_dynamic(A):
    lower_sum = 0
    min_distance = None

    for i in range(len(A)):
        # update lower sum immediately
        lower_sum += A[i]
        # calculate upper sum
        upper_sum = sum(A[i+1:])
        # check the distance of this split
        distance = abs(lower_sum-upper_sum)

        # use it, if it is better than the last best split
        if (min_distance is None) or (distance < min_distance):
            min_distance = distance
            min_distance_index = i+1

    return min_distance_index

# driver code
print(find_equilibrium_dynamic([1,4,2,0,3,8,-4])) #3     