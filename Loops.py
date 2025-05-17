# Task 1 - Countdown Timer
start = int(input("Enter the starting number: "))  # Taking user input
while start > 0:
    print(start, end=' ')
    start -= 1
print("Blast off!")

print("\n" + "-"*40 + "\n")  # Separator for clarity

# Task 2 - Multiplication Table
num = int(input("Enter a number: "))  # Taking user input
print("Multiplication table for", num,":")
for i in range(1, 11):
    print(num," x ",i, " = ", num * i)

print("\n" + "-"*40 + "\n")  # Separator for clarity

# Task 3 - Factorial Calculator
fact_num = int(input("Enter a number: "))  # Taking user input
factorial = 1
for i in range(1, fact_num + 1): # Should not start with 0, else result will be 0
    factorial *= i
print("The factorial of ",fact_num," is ",factorial)
