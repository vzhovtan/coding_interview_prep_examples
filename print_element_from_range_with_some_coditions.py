"""
Print digit from 1 to 100 with the following conditions: 
if divided by 4 and 6 print LinkedIn, 
if divided by 4 only print In, 
if divied by 6 only print Linked
"""

for i in range (1, 101):
    if i%4 == 0 and i%6 == 0:
        print("LinkedIn")
    elif i%6 == 0:
        print("In")
    elif i%4 == 0:
        print("Linked")
    else:
        print(str(i))            