"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
For example,
"A man, a plan, a canal: Panama" is a palindrome. "race a car" is not a palindrome.
"""

def palindrom_recursion (s):
    if len(s) <= 1:
        return True
    else:
        if s[0] == s[-1]:
            print(s[0], s[-1])
            print(s[1:-1])
            return palindrom_recursion(s[1:-1])
        else:
            return False    

# driver code
s = " Kanakanak   "
inp = s.lower().replace(" ", "")
print(palindrom_recursion(inp))