"""
Insertion sort
"""

def insert_sort(arr):
    length = len(arr)
    for i in range (0, length):
        insert_element = arr[i] # new unsorted element
        insert_position = i # poistion we are working on
        for j in range(insert_position-1, -1, -1):
            if insert_element < arr[j]:
                arr[j+1] = arr[j] # if the new element is smaller than the sorted element, sorted element is shifted to the right
                insert_position -= 1 # shift position to the left
                arr[insert_position] = insert_element   # insert new unsorted element in place of sorted element
    return arr            

# driver code
a_list = [5, 6, 7, 8, 9, 0, 1, 2, 3, 4]
print(insert_sort(a_list))