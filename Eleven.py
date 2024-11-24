#This program prints out the price of an item
price = int(input("Input item price: "))
tax = 12
total_price = price + (price*tax/100)
print(f"The price of the item is {total_price}ugx.")