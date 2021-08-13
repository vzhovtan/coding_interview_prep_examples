"""
Given an array with positive number the task is that we find largest subset from array that contain elements which are Fibonacci numbers.
Input  : arr = [0, 2, 8, 5, 2, 1, 4, 13, 23]
Output : subset = [0, 2, 8, 5, 2, 1, 13, 23]
"""

def find_subset(arr):
    answer = []
    fib_list = fib(max(arr))
    for i in range(len(arr)):
        if arr[i] in fib_list:
            answer.append(arr[i])
    return answer

def fib(n):
    res = [0, 1]
    stack = [0, 1] 
    if n in [0, 1]:
        return 1
    else :
        while n > 1:
            stack.append(sum(stack))
            res.append(stack[-1])
            stack.pop(0)
            n -= 1 
    return res

if __name__ == "__main__":
    array = [0, 2, 8, 5, 2, 1, 4, 13, 23]
    print(find_subset(array))
