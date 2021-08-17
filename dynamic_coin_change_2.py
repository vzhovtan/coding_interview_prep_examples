"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1
"""

def dpMakeChange(coinValueList,change,minCoins,coinsUsed):
   for cents in range(change+1):
      coinCount = cents
      newCoin = 1
      for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
               coinCount = minCoins[cents-j]+1
               newCoin = j
      minCoins[cents] = coinCount
      coinsUsed[cents] = newCoin
   return minCoins[change]

def printCoins(coinsUsed,change):
   coin = change
   while coin > 0:
      thisCoin = coinsUsed[coin]
      print(thisCoin)
      coin = coin - thisCoin

# driver code    
amnt = 63
clist = [1,5,10,21,25]
coinsUsed = [0]*(amnt+1)
coinCount = [0]*(amnt+1)

print("Making change for",amnt,"requires")
print(dpMakeChange(clist,amnt,coinCount,coinsUsed),"coins")
print("They are:")
printCoins(coinsUsed,amnt)
print("The used list is as follows:")
print(coinsUsed)
