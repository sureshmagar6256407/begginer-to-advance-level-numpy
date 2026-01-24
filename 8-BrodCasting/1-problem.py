prices = [10,30,40]
discount  = 10  
final_prices  = []  
for price in prices :
    final_price = price- (price * discount / 100)
    final_prices.append(final_price)
print(final_prices)

#this is very slow in to much data