"""
Find lenght of longest non-consequtive subsequence between two strings
"""

def find_long_comm(s1, s2, m, n):
    table = [[0 for x in range(m+1)]for x in range(n+1)]
    print(table)

    for i in range (1,m+1):
        for j in range(1,n+1):
            if s1[i-1] == s2[j-1]:
                table[i][j] = table[i-1][j-1] + 1
            else:
                table[i][j]  = max(table[i-1][j], table[i][j-1])
    print(table)
    return table[m][n]              

# driver code
s1 = "ABCDGHF" 
s2 = "AEBCSHT"
m = len(s1)
n = len(s2)
print(find_long_comm(s1, s2, m, n))