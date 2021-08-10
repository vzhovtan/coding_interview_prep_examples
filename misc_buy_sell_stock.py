"""
Given a array of numbers representing the stock prices of a company in  chronological order, write a function that calculates the maximum profit 
you could have made from buying and selling that stock once. You must buy  before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you 
could buy the stock at 5 dollars and sell it at 10 dollars.
"""

def buy_and_sell(l):
    max_profit, current_max = 0, 0 
    for price in reversed(l):                           #loop through reversed list
        print("curr price", price)
        current_max = max(current_max, price)           #get current maximum - compare current maximum with current price
        print("curr max", current_max)               
        potential_profit = current_max - price          #get potential profit - current maximum minus current price
        print("pot profit", potential_profit)          
        max_profit = max(potential_profit, max_profit)  #get max of profit
    return max_profit

def most_profit(stock):
	max_profit = 0
	for i in range(len(stock)):
		profit = 0
		for j in range(i+1, len(stock)):
			profit = stock[j] - stock[i]
			# print(stock[j], stock[i])
			if  profit > max_profit:
				max_profit = profit

	return max_profit

# driver code
print(buy_and_sell([9, 11, 8, 5, 7, 10])) #5
print(buy_and_sell([])) #0
print(buy_and_sell([1])) #0
print(buy_and_sell([1, 2, 8, 1])) #7

print(most_profit([9, 11, 8, 5, 7, 10])) #5
print(most_profit([])) #0
print(most_profit([1])) #0
print(most_profit([1, 2, 8, 1])) #7
