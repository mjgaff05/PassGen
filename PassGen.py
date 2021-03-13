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
input_set = input("Enter the corresponding numbers of character sets to include, separated by a comma.\n1) Numbers\n2) Upper Case\n3) Lower Case\n4) Special\n").split(",")
print(input_set)

numbers = "0123456789"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case = "abcdefghijklmnopqrstuvwxyz"
special = "!#$%&()+<=>?@^~"


char_set = ""
chars = ""
num = 0
uc = 0
lc = 0
spec = 0
for x in input_set:
 	if x == '1':
 		num = 1
 	elif x == '2':
 		uc = 1
 	elif x == '3':
 		lc = 1
 	elif x == '4':
 		spec = 1
 	else:
 		char_set = "Invalid Set"

#Function to ask user whether to make up random chars or input strings
#input_text = input("Do you want to enter a word to use in the password? (Y/N) ")
#if input_text == ("Y"):
	#Take user strings
#	string1 = input("Enter a random word. ")
#elif input_text == ("N"):
#	string1 = "random_chars"
#else:
#	string1 = "Invalid Entry"

#Get characters for the password
pass_chars = ""
if spec == 1:
	pass_chars = pass_chars + random.choice(special) + random.choice(special)
if num == 1:
	pass_chars = pass_chars + random.choice(numbers) + random.choice(numbers)
for x in range(len(pass_chars), num_digits):
	pass_chars = pass_chars + random.choice(upper_case + lower_case)
	
#Mix up the password

#Output password
password = pass_chars
print(password)