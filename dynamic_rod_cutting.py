"""
Given a rod of length n inches and an array of prices that includes prices of all pieces of size smaller than n. 
Determine the maximum value obtainable by cutting up the rod and selling the pieces. 
For example, if the length of the rod is 8 and the values of different pieces are given as the following, 
then the maximum obtainable value is 22 (by cutting in two pieces of lengths 2 and 6) 
length   | 1   2   3   4   5   6   7   8  
--------------------------------------------
price    | 1   5   8   9  10  17  17  20
"""

class RodCutting:	
	def __init__(self, lengthOfRod, prices):
		self.lengthOfRod = lengthOfRod
		self.prices = prices
		self.dpTable = [ [0]*(lengthOfRod+1) for x in range(len(prices)) ]
	
	def dynamicProgrammingApproach(self, lengthOfRod, prices):
		# 2 for loops to make sure the first row / column have all zeros !!!
		for i in range(1,len(self.prices)):
			for j in range(1,self.lengthOfRod+1):
				if i <= j:
					self.dpTable[i][j] = max(self.dpTable[i-1][j], self.prices[i]+self.dpTable[i][j-i])
				else:
					self.dpTable[i][j] = self.dpTable[i-1][j]
		
	def showResults(self):
		print("Max profit is: $%d" % self.dpTable[len(self.prices)-1][self.lengthOfRod])
		columnIndex = self.lengthOfRod
		rowIndex = len(self.prices)-1
		while columnIndex > 0 or rowIndex > 0:
			if self.dpTable[rowIndex][columnIndex] == self.dpTable[rowIndex-1][columnIndex]:
				rowIndex = rowIndex - 1
			else:
				print("We make cut: ", rowIndex,"m")
				columnIndex = columnIndex - rowIndex
		
# driver code
lengthOfRod = 13
prices = [0,2,5,7,3]
rodCutting = RodCutting(lengthOfRod, prices)
rodCutting.dynamicProgrammingApproach(lengthOfRod, prices)
rodCutting.showResults()

	
	
		
	