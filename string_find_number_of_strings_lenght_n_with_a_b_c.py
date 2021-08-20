"""
Given a length N, count the number of strings of length N that can be made using ‘a’, ‘b’ and ‘c’ with at-most one ‘b’ and two ‘c’s allowed.
One solution is:
- Find all the possible combinations of aCount, bCount, cCount to form the string of length n;
Ex: n = 3 : 
aCount = 3, bCount = 0, cCount = 0; meaning there are 3 'a's, 0 'b' and 0 'c'in that string
aCount = 2, bCount = 1, cCount = 0;
aCount = 1, bCount = 1, cCount = 1;
.....
- Eliminate combinations that don't meet the criteria which is bCount <= 1 and cCount <= 2;
- For each combinations, calculate the number of distinct permutations
Ex: n = 4 : aCount = 2, bCount = 0, cCount = 2 ----> totalPermutations = n! / (aCount!*bCount!*cCount!) (This is a formulas for finding number of distict permutations)
In this case it would be 4!/(2!*0!*2!) = 6
- Add them all up to get the answer
"""

def solution(n):
    aCount, bCount, cCount, answer = 0, 0, 0, 0
    for a in range(n):
        aCount = a
        for b in range(n-aCount):
            bCount = b
            if bCount > 1:
                continue
            cCount = n - (aCount + bCount)
            if cCount > 2:
                continue

        print(aCount + " " + bCount + " " + cCount)
        answer = answer + (Factorial(n) / (Factorial(aCount) * Factorial(bCount) * Factorial(cCount)))
    
    return answer
    
def Factorial(n):
    result = 1
    for i in range(n):
        result = result * i
    return result

def count_abc(n, nb, nc):
    if n == 1:
        return 1 + (1 if nb else 0) + (1 if nc else 0)
    
    result = count_abc(n-1, nb, nc)
    if nb > 0:
        c2 = count_abc(n-1, nb-1, nc)
        result += c2
    if nc > 0:
        c3 = count_abc(n-1, nb, nc-1)
        result += c3
    return result


# driver code
print(count_abc(1, 1, 2))
print(count_abc(2, 1, 2))
print(count_abc(3, 1, 2))
print(count_abc(4, 1, 2))
print(count_abc(5, 1, 2))
print(count_abc(6, 1, 2))
print(count_abc(7, 1, 2))
print(count_abc(100, 1, 2))