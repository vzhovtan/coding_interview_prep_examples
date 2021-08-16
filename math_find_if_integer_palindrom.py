"""
Determine whether an integer is a palindrome. An integer is a palindrome 
when it reads the same backward as forward.
"""

def isPalindrome(x):
    return str(x) == str(x)[::-1]

# driver code
print(isPalindrome(121))
print(isPalindrome(-121))