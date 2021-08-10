"""
Given a set of items, each with a weight and a value, determine the number of each item to include in a 
collection so that the total weight is less than or equal to a given limit and the total value is as large as possible
"""

class Knapsack:
	def __init__(self, numOfItems, capacityOfKnapsack, weightOfItems, profitOfItems):
		self.numOfItems = numOfItems
		self.capacityOfKnapsack = capacityOfKnapsack
		self.weightOfItems = weightOfItems
		self.profitOfItems = profitOfItems
		self.dpTable = [[0 for x in range(capacityOfKnapsack+1)] for x in range(numOfItems+1)]
	
	def dynamicProgrammingApproach(self):	
		# no need to initialize because there are 0s by default !!!
		for i in range(1,self.numOfItems+1):
			for w in range(1,self.capacityOfKnapsack+1):
				notTakingItem = self.dpTable[i-1][w]
				takingItem = 0
				if self.weightOfItems[i] <= w:
					takingItem = self.profitOfItems[i] + self.dpTable[i-1][w-self.weightOfItems[i]]
				self.dpTable[i][w] = max( notTakingItem, takingItem )
		
	def showResult(self):

		print("Total benefit: %d" % self.dpTable[self.numOfItems][self.capacityOfKnapsack], "\n", self.dpTable)
		w = self.capacityOfKnapsack		
		for n in range(self.numOfItems,0,-1):
			if self.dpTable[n][w] !=0 and self.dpTable[n][w] != self.dpTable[n-1][w]:
				print("We take item #%d" % n )
				w = w - self.weightOfItems[n]

# driver code
numOfItems = 4
capacityOfKnapsack = 7
weightOfItems = [10,1,3,4,5]
profitOfItems = [2,1,4,5,7]

knapsack = Knapsack(numOfItems, capacityOfKnapsack, weightOfItems, profitOfItems)
knapsack.dynamicProgrammingApproach()
knapsack.showResult()