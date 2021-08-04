"""
Merge two sorted arrays and keep the resulted array sorted
"""

def merge_two_sorted(arr1, arr2):
    size_1 = len(arr1) 
    size_2 = len(arr2) 
    res = [] 
    i, j = 0, 0
  
    while i < size_1 and j < size_2: 
        if arr1[i] < arr2[j]: 
          res.append(arr1[i]) 
          i += 1
        else: 
          res.append(arr2[j]) 
          j += 1
      
    res = res + arr1[i:] + arr2[j:]
    return res 

# driver code
test_list1 = [1, 5, 6, 9, 11] 
test_list2 = [3, 4, 7, 8, 10] 
print ("The combined sorted list is : ", merge_two_sorted(test_list1, test_list2)) 