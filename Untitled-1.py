monthlyinterest = (5.2/100)/12
print (monthlyinterest)
balance = (320000*((1+monthlyinterest)**60)) - (1757.15*((((1+monthlyinterest)**60)-1)/monthlyinterest))
print(balance)