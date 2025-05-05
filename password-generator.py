import random
#Listing of upper case letters
upper_case_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#Listing of lower case letters
lower_case_letters = "abcdefghijklmnopqrstuvwxyz"

#Listing of numbers
numbers = "0123456789"

#Listing of symbols
symbols = "`~!@#$%^&*<>[]/+_=;'?|()"

#Adding of the variables
all_characters = upper_case_letters + lower_case_letters + numbers + symbols

#Requesting for an input figure of password to generate
password_lengh = int(input("Enter a length: "))

Generated_password = ''.join(random.sample(all_characters, password_lengh))
print("Generated password:", Generated_password)