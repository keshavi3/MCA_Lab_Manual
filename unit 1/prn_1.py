 #Write a program to get input from the user for principal (p), rate (r), and time (n)

p = float(input("Enter the principal amount (p): "))
r = float(input("Enter the annual interest rate (r): "))
n = float(input("Enter the time period (n): "))

si = (p * r * n) / 100

print("The simple interest (si) is:", si)