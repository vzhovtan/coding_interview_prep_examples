"""
Create function to convert integer to string 
Simple function using Python features
"""

data = 234

bn = format(data, 'b')
ot = format(data, 'o')
dec = format(data, 'd')
hx = format(data, 'x')

print(type(bn), type(ot), type(dec), type(hx))
print(bn, ot, dec, hx)