"""
Given a string, find the length of the longest substring without repeating characters. For example, 
the longest substring without repeating letters for “abcabcbb” is “abc”, which the length is 3. 
For “bbbbb” the longest substring is “b”, with the length of 1.
"""

def longest_1(inp):
    last_seen = {}
    longest = [0,1]
    startIdx = 0
    for idx, letter in enumerate(inp):
        if letter in last_seen.keys():
            startIdx = max (startIdx, last_seen[letter] + 1)
        if longest[1] - longest[0] < idx + 1 - startIdx:
            longest = [startIdx, idx + 1]
        last_seen[letter] = idx    

    return inp[longest[0]:longest[1]]   #returning the substring itself

def longest_2(string):        
    #Creating a dict to store the last positions of occurrence 
    seen = {} 
    maximum_length = 0
    #Starting the inital pointer of window to index 0 
    start = 0 

    for ind in range(len(string)): 
        #Checking if we have already seen the element or not 
        if string[ind] in seen:
            #If we have seen the number, move the start pointer to position after the last occurrence 
            start = max(start, seen[string[ind]] + 1) 
        # Updating the last seen value of the character 
        seen[string[ind]] = ind
        maximum_length = max(maximum_length, ind - start + 1) 
        print(seen, "MaxLenght", maximum_length, "Start", start, "Ind", ind)

    return maximum_length   # returning the lenght

# driver code
inp = "clementisacap"
print(longest_1(inp))            
print(longest_2(inp)) 
             



