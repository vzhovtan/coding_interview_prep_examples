"""
Find lenght of longest non-consequtive subsequence between two strings
"""

def find_long_comm(s1, s2, n, m):
    if n == 0 or m == 0:
        return 0
    
    if s1[n-1] == s2[m-2]:
        return 1 + find_long_comm(s1, s2, n-1, m-1)
    else: 
        return max(find_long_comm(s1, s2, n, m-1), find_long_comm(s1, s2, n-1, m))

# driver code
s1 = "ABCDGHF" 
s2 = "AEBCSHT"
n = len(s1)
m = len(s2)
print(find_long_comm(s1, s2, n, m))