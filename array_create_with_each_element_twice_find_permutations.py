"""
Given an integer 'n', create an array such that each value is repeated twice. For example
n = 3 -> [1,1,2,2,3,3]
n = 4 -> [1,1,2,2,3,3,4,4]

After creating it, find a permutation such that each number is spaced in such a way,
they are at a "their value" distance from the second occurrence of the same number.
For example: n = 3 -> This is the array - [1,1,2,2,3,3]
Your output should be [3,1,2,1,3,2]
The second 3 is 3 digits away from the first 3.
The second 2 is 2 digits away from the first 2.
The second 1 is 1 digit away from the first 1.

Return any 1 permutation if it exists. Empty array if no permutation exists.
"""

def back_track(buf, n):
    N = len(buf)
    if (n == 0):
        print(buf)
        return
    for i in range(N - n - 1):
        j = i + n + 1
        # print(buf, N, n, i, j) uncomment to debug
        if buf[i] != 0 or buf[j] != 0:
            continue
        buf_next = list(buf) # using deep copy
        buf_next[i] = buf_next[j] = n
        back_track(buf_next, n-1)

def main(n):
    buf = [0] * n * 2 # get the buf
    back_track(buf, n)
    
# driver code    
print("== back tracking == ")
main(4)