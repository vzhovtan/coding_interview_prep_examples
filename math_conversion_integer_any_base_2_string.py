"""
Create a function to convert provided number to string with provided base
"""

def digit_to_char(digit):
    if digit < 10: 
        #return chr(ord('0') + digit)
        return (str(digit))
    else: 
        return chr(ord('a') + digit - 10)

def str_base(number,base):
    if number < 0:
        return '-' + str_base(-number,base)
    else:
        (d,m) = divmod(number,base)
        print(d, m)
        if d:
            return str_base(d,base) + digit_to_char(m)
        else:
            return digit_to_char(m)

def to_str(n,base):
   convertString = "0123456789ABCDEF"
   if n < base:
      return convertString[n]
   else:
      return to_str(n//base,base) + convertString[n%base]

# driver code
print(str_base(40, 20))
print(to_str(40, 20))
