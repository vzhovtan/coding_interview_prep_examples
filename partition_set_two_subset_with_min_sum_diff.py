"""
Create a function to partition given set to two subsets with minimal difference between resulted subsets
"""

def findMinRec(arr, i, sumCalculated, sumTotal):
    #if last element reached.
    #sum of first subset is sumCalculated, 
    #sum of other subset is sumTotal- sumCalculated.  
    #return absolute difference of two sums.
    if (i == 0):
        return abs((sumTotal - sumCalculated) - sumCalculated)
    #for every item arr[i], there are two choices
    #(1) not included in first subset
    #(2) included in first subset
    # return minimum of two choice
    return min(findMinRec(arr, i - 1, sumCalculated+arr[i - 1], sumTotal),
               findMinRec(arr, i - 1, sumCalculated, sumTotal))
 
#returns minimum possible difference between sums of two subsets
def findMin(arr,  n):
    sumTotal = sum(arr)
    return findMinRec(arr, n, 0, sumTotal)
 
# driver code
arr = [3, 1, 4, 2, 2, 1]
n = len(arr)
print("The minimum difference between two sets is ", findMin(arr, n))