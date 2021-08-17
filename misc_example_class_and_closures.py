class NthRoot:
    def __init__(self, n=2):
        self.n = n
    
    def set_root(self,n):
        self.n = n
    
    def calc(self, x):
        return x ** (1/self.n)

def nth_root(n=2):
    def calc(x):
        return x ** (1/n)
    return calc

# driver code    
thirdRoot = NthRoot(3)
print("Class example ", thirdRoot.calc(27))

third_root = nth_root(3)
print("Closure example ", third_root(27))