"""
Given an input string s, reverse the string word by word.
For example, given s = "the sky is blue", return "blue is sky the".
"""

def rev(strng):
    if " " not in strng:
        return strng
    else:
        for i in range(len(strng)-1, -1, -1):
            if strng[i] == " ":
                last_word = strng[i+1:]
                # print(last_word)
                strng = strng[:i]   
                break
    
        return last_word + " " + rev(strng)

def reverse_words(inp):
    resulted_string = ""
    new_inp = inp.strip().split(" ")
    print(new_inp)
    result = new_inp[::-1]
    for word in result:
        if word == "":
            continue
        word += " "
        resulted_string += word

    print(resulted_string)   

# driver code
strng = "the sky is blue"
print(rev(strng))
reverse_words(strng)