#This program calculates BMI
weight = float(input("Input weight in kgs: "))
height = float(input("Input height in meters: "))
BMI = weight/height**2
print(f"BMI = {BMI}")