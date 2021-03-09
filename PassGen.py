import random
import sys

#Function to take user requirements

#Take first requirement which is length of password (should be an integer)
try:
	num_digits = int(input("How long should your password be? (int) "))
except ValueError:
	print("Error: Number not entered. Exiting passGen.")
	sys.exit(0)

#Take requirements in upper case, lower case, special chars, numbers, etc
char_set = input("Enter the corresponding numbers of character sets to include, separated by a comma.\n1) Numbers\n2) Upper Case\n3) Lower Case\n4) Special ")


#Function to ask user whether to make up random chars or input strings
input_text = input("Do you want to enter a word to use in the password? (Y/N) ")
if input_text == ("Y"):
	#Take user strings
	string1 = input("Enter a random word. ")
if input_text == ("N"):
	string1 = "random_chars"


#Mix up the password

#Output password
password = "Not_secure101" + string1
print(password)