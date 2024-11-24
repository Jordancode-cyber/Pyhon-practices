#This program calculates simple interest
amount = int(input("Input principal amount: "))
rate = float(input("Input annual interest rate(%): "))
time = int(input("Input time(years): "))
SI = (amount*rate*time)/100
print(f"Simple interest value = {SI}ugx")