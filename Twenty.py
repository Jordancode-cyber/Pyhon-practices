#This program checks the status of number
number = int(input("Input a number: "))
if number == 0:
    print("Neutral")
elif number > 0:
    print("Positive")
else:
    print("Negative")