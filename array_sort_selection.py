"""
Selection sort
"""

def findSmallest(arr): # Finds the smallest value in an array 
	smallest = arr[0] # Stores the smallest value
  	# Stores the index of the smallest value
	smallest_index = 0
	for i in range(1, len(arr)):
		if arr[i] < smallest:
			smallest_index = i
			smallest = arr[i]      
  	
	return smallest_index

# Sort array
def selectionSort(arr):
	newArr = []
	for _ in range(len(arr)): # Finds the smallest element in the array and adds it to the new array
		smallest = findSmallest(arr)
		newArr.append(arr.pop(smallest))
  	
	return newArr

# driver code
array = [1, -5, 7, 70, 80, 30, 22, 18, 27, 3, 40, 50]
print(selectionSort(array))
