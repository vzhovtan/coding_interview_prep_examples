def deco(f):
    def g(*args, **kwargs):
        print("Calling ", f.__name__)
        return f(*args, **kwargs)
    return g

def func(x):
    return 2*x
func = deco(func)
print(func(2))

# with synctactic shugar
def deco1(f):
    def g(*args, **kwargs):
        print("Calling ", f.__name__)
        return f(*args, **kwargs)
    return g
    
@deco
def func1(x):
    return 2*x

print(func1(2))