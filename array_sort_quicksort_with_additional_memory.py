"""
Quick sort with additional memory

"""
def quicksort(array):
  if len(array) < 2:
    # base case, arrays with 0 or 1 element are already "sorted"
    return array
  else:
    # recursive case
    pivot = array[-1]
    print(f"pivot is {pivot} \n")
    # sub-array of all the elements less than the pivot
    less = [i for i in array[:-1] if i <= pivot]
    print(f"less one {less} \n")
    # sub-array of all the elements greater than the pivot
    greater = [i for i in array[:-1] if i > pivot]
    print(f" greater one {greater} \n")
    return quicksort(less) + [pivot] + quicksort(greater)

# driver code
print(quicksort([1, -5, 7, 70, 80, 30, 22, 18, 27, 3, 40, 50]))
