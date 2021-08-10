class Fibonacci:
	def __init__(self):
		self.MemoizeTable = {}  # O(1)
		self.MemoizeTable[0] = 0
		self.MemoizeTable[1] = 1
	
	def fibonacciMemoize(self, n):
		if n in self.MemoizeTable:
			return self.MemoizeTable[n]
		self.MemoizeTable[n-1] = self.fibonacciMemoize(n-1)
		self.MemoizeTable[n-2] = self.fibonacciMemoize(n-2)
		calculatedNumber = self.MemoizeTable[n-1] + self.MemoizeTable[n-2] # O(1)
		self.MemoizeTable[n] = calculatedNumber
	
		return calculatedNumber
	
	def naiveApproach(self, n):
		# f(n) = f(n-1) + f(n-2) where f(0) = 0 and f(1) = 1
		if n == 0: return 0
		if n == 1: return 1
		
		return self.naiveApproach(n-1) + self.naiveApproach(n-2)
		
# driver code
fibonacci = Fibonacci()
print( fibonacci.naiveApproach(10) )
print( fibonacci.fibonacciMemoize(100) )
		
	