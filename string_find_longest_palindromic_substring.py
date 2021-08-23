"""
Given a string S, find the longest palindromic substring in S. 
You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
"""

def longest_palindrom(string):
    current_longest = [0, 1]
    for idx in range(1, len(string)):
        odd = get_longest_palindrom(string, idx-1, idx+1)
        even = get_longest_palindrom(string, idx-1, idx)
        longest = max(odd, even, key = lambda x: x[1] - x[0])
        current_longest = max(longest, current_longest, key = lambda x: x[1] - x[0])
    
    return string[current_longest[0]:current_longest[1] + 1]

def get_longest_palindrom(string, left_idx, right_idx):
    while left_idx >= 0 and right_idx <len(string):
        if string[left_idx] != string[right_idx]:
            break
        left_idx -= 1
        right_idx += 1

    return [left_idx+1, right_idx]    

string = "abacddcaba"
print(longest_palindrom(string))


