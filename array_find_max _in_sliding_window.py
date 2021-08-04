"""
Find max element in sliding windows with size K using queue - enqueue K elements into the queue, 
calculate max, pop first element, enqueue new element, calculate new max, add to the list of max
"""

def find_max_sliding(arr, k):
    curr_max = 0
    max_sum = 0
    que = []

    for j in range(k):
        que.append(arr[j])
    curr_max = sum(que)
    print(que)
    max_sum = max(max_sum, curr_max)    

    i = k 
    while i < len(arr):
        que.append(arr[i])
        que.pop(0)
        print(que)
        curr_max = max(que)
        max_sum = max(max_sum, curr_max)
        i += 1
    return max_sum

# driver code
arr = [x for x in range(10)]
print(arr)
print(find_max_sliding(arr, 2))


        
