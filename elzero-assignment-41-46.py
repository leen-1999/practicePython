# 01
num1 = int(input("first num").strip())
num2 = int(input("second num").strip())
operation = input("type operation + or - or * or / or %").strip()

if operation == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif operation == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif operation == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif operation == "/":
    print(f"{num1} / {num2} = {num1 / num2}")
elif operation == "%":
    print(f"{num1} % {num2} = {num1 % num2}")
else:
    print("error")

# 02
age = 17
print("App Is Suitable For You") if age > 16 else print(
    "App Is Not Suitable For You")

# 03
age = int(input("enter age "))
if age > 10 and age < 100:
    print(f"your age in months is {age * 12} months")
    print(f"your age in weeks is {(age * 12)*4} weeks")
    print(f"your age in days is {age * 365} days")
    print(f"your age in hours is {(age * 12*4 *7)*24} hours")
    print(f"your age in mintutes is {(age * 12*4 *7*24)*60} minutes")
    print(f"your age in seconds is {(age * 12*4 *7*24 *60 )*60} seconds")
else:
    print("out range")

# 04

Countries = ["Lebanon", "Syria", "Egypt",
             "Palestine", "Germany", "Sweden", "Canada"]
price = 100
discount = 30
country = input("enter you country").strip().capitalize()
if country in Countries:
    print(
        f"Your Country Eligible For Discount And The Price After Discount Is {int(price-(price * 30/100))}$")
else:
    print(f"Your Country Not Eligible For Discount And The Price Is {price}$")
