#This program prints Hello World to console
A = "Hello, "
B = "World!"
print(A + B)

value = "Hello, World!"
print(value)

#This program prints out the user's name
name = str(input("Please input your name: "))
print(f"Hello, {name}!")

#This program adds two numbers given by the user
num1 = int(input("Input first number: "))
num2 = int(input("Input second number: "))
value = num1+num2
print(f"The sum of your two numbers is {value}.")

#This program prints out user's age
year_of_birth = int(input("Enter year of birth: "))
current_year = 2024
age = current_year-year_of_birth
in_5_years = age + 5
print(f"You are {age} years old and in 5 years you will be {in_5_years} old.")

#This program prints out the area of a circle
r = float(input("Please input your radius value: "))
pi = 3.1416
area = pi*r*r
print(f"Area is = {area}")

#This program calculates the perimeter of a rectangle
length = int(input("Length value: "))
width = int(input("Width value: "))
perimeter = 2*(length+width)
print(f"Perimeter = {perimeter}")

#This program converts fahrenheit to celsius
celsius = float(input("Celsius value: "))
fahrenheit = (celsius* 9/5) + 32
print(f"Temp in fahrenheit is {fahrenheit} degrees.")

#This program multiplies two numbers
num1 = int(input("First num: "))
num2 = int(input("Second num: "))
value = num1*num2
print(f"Value is {value}")

#This program calculates the value of a cylinder
r = float(input("Radius value: "))
h = float(input("Height value: "))
pi = 22/7
volume = pi*(r**2)*h
print(f"Volume = {volume}")

#This program calculates BMI
weight = float(input("Input weight in kgs: "))
height = float(input("Input height in meters: "))
BMI = weight/height**2
print(f"BMI = {BMI}")

#This program prints out the price of an item
price = int(input("Input item price: "))
tax = 12
total_price = price + (price*tax/100)
print(f"The price of the item is {total_price}ugx.")

#This program prints user's current age
year_of_birth = int(input("Input year of birth: "))
current_year = 2024
age = current_year-year_of_birth
print(f"You are {age} years old.")

#This program prints the area of a square
length = int(input("Input length of side: "))
area = 4*length
print(f"Area = {area}cm squared")

#This program calculates simple interest
amount = int(input("Input principal amount: "))
rate = float(input("Input annual interest rate(%): "))
time = int(input("Input time(years): "))
SI = (amount*rate*time)/100
print(f"Simple interest value = {SI}ugx")

#This program coverts km to miles
km = float(input("Input distance in km: "))
miles = km*0.621371
print(f"Miles covered = {miles}")

#This program prints name in reverse order
fname = str(input("Input first name: "))
lname = str(input("Input second name: "))
print(lname + fname)

#This program prints the area of a triangle
base = int(input("Base: "))
height = int(input("Height: "))
area = 0.5*base*height
print(f"Triangle area = {area}cm squared")

#This program calculates average speed
distance = int(input("Distance traveled in km: "))
time = int(input("Time in hours: "))
average_speed = distance/time
print(f"Average speed is {average_speed} km/s")

#This program coverts time
seconds = float(input("Input number in seconds: "))
hours = seconds/3600
minutes = seconds/60
seconds = seconds
print(f"The result is {hours}hrs, {minutes}min, {seconds}s ")

#This program checks the status of number
number = int(input("Input a number: "))
if number == 0:
    print("Neutral")
elif number > 0:
    print("Positive")
else:
    print("Negative")