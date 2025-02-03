#write a program to input 2 numbers and one arithmetic operator and perform operations as per arithmetic operator which is given as input 

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the arithmetic operator (+, -, *, /): ")

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
          print= (num1 / num2)
    else:
        print= ("Error! Division by zero is not allowed")
else:
    print("Error: Invalid operator.")



