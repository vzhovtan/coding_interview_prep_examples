"""
find all permutations of S existing in B
"""

def find_perm(s, b):    
    result = 0
    len_b = len(b)
    len_s = len(s)

    for i in range(len_b - len_s):
        temp_sum = 0
        temp = []
        for j in range(len_s):
            if b[i+j] in s:
                temp_sum += 1
                temp.append(b[i+j])
            else:
                break
        # print(temp)
        # print(b[i:i+len_s])    
        if temp_sum == 4:
            result += 1

    return result                

# driver code
s = "abbc"
b  = "babcddaefdbbacbddfae"
print(find_perm(s, b))
