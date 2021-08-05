"""
Given a array which initially contains 0, the following queries can be performed:
0 X: add X to the list
1 X: replace each element “A” of the list by A^X, where ^ is the xor operator
Return a list with the result elements in increasing order.

Input: 5 (no of queries)
0 4
0 2
1 4
0 5
1 8
Result: 8 12 13 14
"""

def query(arr, type, elem):
    if type == 0: 
        arr.append(elem)
    elif type == 1:
        for index, value in enumerate(arr):
            value = value ^ elem
            arr[index] = value
    arr.sort()
    return arr

# driver code
res = []
res = query(res, 0, 4)
print(res)
res = query(res, 0, 2)
print(res)
res = query(res, 1, 4)
print(res)
res = query(res, 0, 5)
print(res)
res = query(res, 1, 8)
print(res)


    
                

