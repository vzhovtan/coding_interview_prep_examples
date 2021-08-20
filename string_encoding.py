"""
Run-length encoding is a fast and simple method of encoding strings. 
The basic idea is to represent repeated successive characters as a single count and character. 
For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding. You can assume the string  to be encoded have no digits and consists solely of 
alphabetic characters. You can assume the string to be decoded is valid.
"""
import itertools

def encode(s):
    encoded = ""
    counter = 1
    last_seen = s[0]

    for i in range(1, len(s)):
        if last_seen == s[i]:
            counter += 1
        else:
            encoded += str(counter) + last_seen
            counter = 0
            last_seen = s[i]
            counter += 1

    #append last last_seen to encoded
    encoded += str(counter) + last_seen

    return encoded

def pythonic_encode(s):
    out = ""
    for item in [list(g) for k, g in itertools.groupby(s)]:
        out = out + str(len(item)) + item[0]

    return out    

# driver code
print(encode("AAAABBBCCDAA")) #4A3B2C1D2A
print(encode("AAAABBBCCDAABDAAAA")) #4A3B2C1D2A1B1D4A
print(encode("AAAABBBCCDAABDAAAAC")) #4A3B2C1D2A1B1D4AC

print(pythonic_encode("AAAABBBCCDAA")) #4A3B2C1D2A
print(pythonic_encode("AAAABBBCCDAABDAAAA")) #4A3B2C1D2A1B1D4A
print(pythonic_encode("AAAABBBCCDAABDAAAAC")) #4A3B2C1D2A1B1D4AC