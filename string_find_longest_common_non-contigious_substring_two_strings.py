"""
Finding max commonf non-contigious substring between two strings with dynamic programming approach
There are 2 func - one for the string and another one for the leght
Leng of string is important so comparison is done as first step in main finc
"""

def sbstr(a, b):
    sbstr = ""
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]: # match
                sbstr += a[i]
                break
    return sbstr

def find_mx(a, b):
    cell = [[0 for i in range(len(b))] for j in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]: # match.
                cell[i][j] = cell[i-1][j-1] + 1
            else: # don't match.
                cell[i][j] = max(cell[i-1][j], cell[i][j-1])
    return cell

# driver code
a = list("ala") 
b = list("aba")
if len(a) > len(b):
    a,b = b,a

print(find_mx(a,b))
print("Leng of max substring is", find_mx(a,b)[-1][-1])  
print("Substring is ", sbstr(a,b))     


