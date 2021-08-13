"""
Given a number n, find the smallest number that has same set of digits as n and is greater than n. 
If n is the greatest possible number with its set of digits, then print “not possible”.
Examples:
For simplicity of implementation, we have considered input number as a string.
Input:  n = "218765"
Output: "251678"
Input:  n = "1234"
Output: "1243"
Input: n = "4321"
Output: "Not Possible"
Input: n = "534976"
Output: "536479"

1) If all digits sorted in descending order, then output is always “Not Possible”. For example, 4321.
2) If all digits are sorted in ascending order, then we need to swap last two digits. For example, 1234.
3) For other cases, we need to process the number from rightmost side (why? because we need to find the smallest of all greater numbers)

Following is the algorithm for finding the next greater number.
I) Traverse the given number from rightmost digit, keep traversing till you find a digit which is smaller than the previously traversed digit. 
For example, if the input number is “534976”, we stop at 4 because 4 is smaller than next digit 9. If we do not find such a digit, then output is “Not Possible”.

II) Now search the right side of above found digit ‘d’ for the smallest digit greater than ‘d’. For “534976″, the right side of 4 contains “976”. 
The smallest digit greater than 4 is 6.

III) Swap the above found two digits, we get 536974 in above example.

IV) Now sort all digits from position next to ‘d’ to the end of number. The number that we get after sorting is the output. For above example, 
we sort digits in bold 536974. We get “536479” which is the next greater number for input 534976.
"""

def find_next_great(n):
    res = list(n)
    answer = ""
    if res == sorted(res, reverse=True):
        return "Not possible"

    if res == sorted(res):
        res[-1], res[-2] = res[-2], res[-1]
        for i in res:
            answer += str(i)
        return answer

    for i in range(len(res)-1, -1, -1):
        if res[i-1] < res[i]:
            smallest = i-1
            next_smallest = sorted(res[smallest+1:])[0]
            for j in range(smallest+1, len(res)):
                if res[j] == next_smallest:
                    res[smallest], res[j] = res[j], res[smallest]
            new_res = sorted(res[smallest+1:])
            del res[smallest+1:]
            for item in new_res:
                res.append(item)         
            break
    for i in res:
        answer += str(i)                              
    return answer                

# driver code
n = "534976"
print(find_next_great(n))    