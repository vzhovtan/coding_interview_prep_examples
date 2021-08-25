"""
Let 1 represent ‘A’, 2 represents ‘B’, etc. Given a digit sequence, count the number of possible decodings of the given digit sequence. 
Examples: 

Input:  digits[] = "121"
Output: 3
The possible decodings are "ABA", "AU", "LA"

This problem is recursive and can be broken in sub-problems. We start from end of the given digit sequence. 
We initialize the total count of decodings as 0. We recur for two subproblems.
1) If the last digit is non-zero, recur for remaining (n-1) digits and add the result to total count.
2) If the last two digits form a valid character (or smaller than 27), recur for remaining (n-2) digits 
and add the result to total count.
"""

def numDecodings(s):  
    return numDecodingsHelper(s,len(s)) 
  
def numDecodingsHelper(s, n): 
    if n == 0 or n == 1 :  
        return 1
    count = 0
    if s[n-1] > "0":  
        count = numDecodingsHelper(s,n-1)  
    if (s[n - 2] == '1' or (s[n - 2] == '2' and s[n - 1] < '7') ) :  
        count += numDecodingsHelper(s, n - 2)  
    return count  
          
# driver code  
digits = "121"
print(numDecodings(digits))  