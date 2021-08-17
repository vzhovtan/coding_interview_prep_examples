import itertools  
 
#itertools.groupby() example
 
arr = "AAAABBBCCDAABDAAAAC"
print([list(g) for k, g in itertools.groupby(arr)])
print([k for k, g in itertools.groupby(arr)])
for item in [list(g) for k, g in itertools.groupby(arr)]:
    print(len(item),item[0])  
