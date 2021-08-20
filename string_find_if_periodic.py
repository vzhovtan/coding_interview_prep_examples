"""
Find whether string S is periodic. Periodic indicates S = nP.
Example
S = "ababab", then n = 3, and P = "ab"
S = "xxxxxx", then n = 1, and P = "xxxxxx"
"""

def factors(n):
    f = []
    for i in range(1, n):
        if n % i == 0:
            f.append(i)
    # print(f)        
    return f

def periodic(s):
    f = factors(len(s))
    for i in f:
        m = len(s)/i
        if s[:i] * int(m) == s:
            # print(i, s[:i], s)
            return True
    return False

# driver code
assert True == periodic("abcabc")
assert True == periodic("abcabcd")