"""
Create a finction which find longest substring in given string containing integers
Both halves of substring have to have the same sum
Example:
Given string is "9430723"
Output is 4, because substring "4307" met the condition
"""

def longest_sub_brute(data):
    n = len(data)
    max_len = 0

    for i in range(n):
        for j in range(i+1, n, 2):
            sub_len = j - i + 1
            if max_len > sub_len:
                continue
            lsum = 0
            rsum = 0
            for k in range(sub_len//2):
                lsum = lsum + int(data[i+k])
                rsum = rsum + int(data[i+k+sub_len//2])
            if lsum == rsum:
                max_len = sub_len    
    
    return max_len

# driver code
data = "9430723"
print(longest_sub_brute(data))


