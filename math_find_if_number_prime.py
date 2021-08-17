"""
Create function to verify if given number is prime
"""

def prime(num):
    # If given number is greater than 1
    if num > 1:
        # Iterate from 2 to n / 2
        for i in range(2, num//2):
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
            print(num, "is a prime number")
            
    else:
        print(num, "is not a prime number")

# driver code
num = 11
prime(num)