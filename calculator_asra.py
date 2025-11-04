#Simple Calculator by Asra Fathima
#Asking the user to enter two numbers 
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
#Asking the user to choose an operation
operation = input("Choose an operation (+, -, *, /): ")
#Performing the operation based on user input
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
      if num2 !=0:
            result = num1/num2 
      else:
           result = "Error: Division by zero is not allowed."
else:
      result = "Invalid operation"
#Display the result
print("Result:", result) 
print("Thank you for using Asra's Calculator!") 