"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
For example,
"A man, a plan, a canal: Panama" is a palindrome. "race a car" is not a palindrome.
"""

def ispalindrom(strng):
    palindrom = True
    i, j = 0, len(strng)-1
    while i < j:
        if strng[i] != strng[j]:
            palindrom = False
        i += 1
        j -= 1
    return palindrom

def checker(data):
    new_data = ""
    for char in data:
        if char.isalpha():
            new_data += char.lower()

    # print(new_data)        
    palindr = True

    for index, char in enumerate(new_data):
        # print(index, char, new_data[len(new_data) - 1 - index])
        if char != new_data[len(new_data) - 1 - index]:
            palindr = False

    return palindr 

# driver code
inp = "abba"
print(ispalindrom(inp.lower()))

data = "A man, a plan, a canal: Panama"
print(checker(data))