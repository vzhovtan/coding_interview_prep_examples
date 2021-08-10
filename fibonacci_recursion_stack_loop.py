import time

def fib_rec(n):
    #simplest one using recursion
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_rec(n-1) + fib_rec(n-2)          

def fib_stack_incr(n):
    #better preformance with stack, increment version
    stack = [0 ,1] 
    if n in [0 ,1]:
        return 1
    else :
        i = 1
        while i < n-1 :
            stack.append(sum(stack))
            stack.pop(0)
            #print(stack)
            i += 1
    return sum(stack)

def fib_stack_decr(n):
    #better preformance with stack, decrement version
    stack = [0 ,1] 
    if n in [0 ,1]:
        return 1
    else :
        while n > 1:
            stack.append(sum(stack))
            stack.pop(0)
            #print(stack)
            n -= 1 
    return stack[-1]

# driver code
start1 = time.time()
print(fib_rec(35))
end1 = time.time()
print("Recursion", "\n", end1-start1, "\n")

start2 = time.time()
print(fib_stack_incr(35))
end2 = time.time()
print("Stack with increment", "\n", end2-start2, "\n")

start3 = time.time()
print(fib_stack_decr(35))
end3 = time.time()
print("Stack with decrement", "\n", end3-start3, "\n")


