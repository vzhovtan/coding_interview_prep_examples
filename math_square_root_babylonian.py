"""
Create a function to calculate square root 
"""

def squareRoot(n): 
    # Using n itself as initial approximation 
    x = n 
    y = 1
    # e decides the accuracy level 
    e = 0.000001
    while(x - y > e): 
    
        x = (x + y)/2
        y = n / x 
    return x 

# driver code
print(squareRoot(16))        