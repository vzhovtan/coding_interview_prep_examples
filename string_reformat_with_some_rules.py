"""
You are given a license key represented as a string S which consists only alphanumeric character and dashes. 
The string is separated into N+1 groups by N dashes.
Given a number K, we would want to reformat the strings such that each group contains exactly K characters, 
except for the first group which could be shorter than K, but still must contain at least one character. 
Furthermore, there must be a dash inserted between two groups and all lowercase letters should be converted to uppercase.

Given a non-empty string S and a number K, format the string according to 
the rules described above.
"""

def licenseKeyFormatting(S, K):
    S = S.split("-")
    S = [letter.upper() for letter in S]
    S = "".join(S)
    S = S[::-1]

    step = K
    new_license = ""

    for i, char in enumerate(S):
    	if i < step:
    		new_license = char + new_license
    	elif i == step:
    		new_license = char + "-" + new_license
    		step = step + K

    return new_license

# driver code
print(licenseKeyFormatting("5F3Z-2e-9-w", 4))
print(licenseKeyFormatting("5F3Z-2e-9-w", 2))
print(licenseKeyFormatting("5F3Z-2e-9-wz", 2))

        