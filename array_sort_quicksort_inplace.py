"""
Quick sort - example from Python Algorithms book by Magnus Lie Hetland
"""

def partition(list, start, end):
    pivot = list[end]                          # Partition around the last value
    bottom = start-1                           # Start outside the area to be partitioned
    top = end                                  # Ditto

    done = 0
    while not done:                            # Until all elements are partitioned...
        while not done:                        # Until we find an out of place element...
            bottom = bottom+1                  # ... move the bottom up.
            if bottom == top:                  # If we hit the top...
                done = 1                       # ... we are done.
                break
            if list[bottom] > pivot:           # Is the bottom out of place?
                list[top] = list[bottom]       # Then put it at the top...
                break                          # ... and start searching from the top.
        while not done:                        # Until we find an out of place element...
            top = top-1                        # ... move the top down.
            if top == bottom:                  # If we hit the bottom...
                done = 1                       # ... we are done.
                break
            if list[top] < pivot:              # Is the top out of place?
                list[bottom] = list[top]       # Then put it at the bottom...
                break                          # ...and start searching from the bottom.
    list[top] = pivot                          # Put the pivot in its place.
    return top                                 # Return the split point


def quicksort(list, start, end):
    if start < end:                            # If there are two or more elements...
        split = partition(list, start, end)    # ... partition the sublist...
        quicksort(list, start, split-1)        # ... and sort both halves.
        quicksort(list, split+1, end)
    else:
        return

if __name__=="__main__":                       # If this script is run as a program:
    list = [5, 6, 7, 8, 9, 0, 1, 2, 3, 4]      # Get all the arguments
    start = 0
    end = len(list)-1
    quicksort(list,start,end)                  # Sort the entire list of arguments
    print (list)                               # Print out the sorted list