# Project: Password Generator
# Developed by: Asra Fathima
# Description: A Python program to generate a strong and random password based on the user's input length
#Password Generator by Asra Fathima
import random
import string
#Defining the characters to use in the password
characters = string.ascii_letters + string.digits + string.punctuation
#Asking the user for the desired password length
length = int(input("Enter the desired password length: "))
#Generating the password
password = ''.join(random.choice(characters) for i in range(length))
#Displaying the generated password
print("Your generated password is:", password)
print("Thank you for using Asra's Password Generator!")