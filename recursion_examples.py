def reverse_str (strng):
    if len(strng) == 1:
        return strng[0]
    else:
        return strng[-1] + reverse_str(strng[:-1]) 


def number_of_paths(n):
    if n < 0:
        return 0
    elif n == 1 or n == 0:
        return 1
    else:        
        return number_of_paths(n - 1) + number_of_paths(n - 2) + number_of_paths(n - 3)

# driver code
arr = "abcdabcdegfhrt"
print("example 1 - original string", arr, "\n")
print("example 1 - reversed string", reverse_str(arr), "\n")
print("example 2 - number of path for staircase with 11 stairs", number_of_paths(11))