#calculator

a = float(input("enter your first number: "))
b = float(input("enter your second number: "))

operator = input("Enter operation (+, -, *, / ):  ")

if  operator == "+":
    print(a + b)
elif operator == "-":
       print(a - b)
elif operator =="*" :
    print(a * b)
elif operator == "/":
    print(a / b)
else:
    print("invalid operations")