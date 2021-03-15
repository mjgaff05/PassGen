import random
import sys

#Function to take user requirements
def getCharSet():
	input_set = input("Do you want to include numbers or special characters?\n1) Numbers\n2) Special\n").split(",")
	print(input_set)

	set_bools = [0,0]
	for x in input_set:
 		if x == '1':
 			set_bools[0] = 1
 		elif x == '2':
 			set_bools[1] = 1
 		else:
 			print("Invalid Set")

	print(set_bools)
	return set_bools



#Take first requirement which is length of password (should be an integer)
try:
	num_digits = int(input("How long should your password be? (int) "))
except ValueError:
	print("Error: Number not entered. Exiting passGen.")
	sys.exit(0)

#Take requirements in upper case, lower case, special chars, numbers, etc
sets = getCharSet()
numbers = "0123456789"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case = "abcdefghijklmnopqrstuvwxyz"
special = "!#$%&()+<=>?@^~"


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
if sets[1] == 1:
	pass_chars = pass_chars + random.choice(special) + random.choice(special)
if sets[0] == 1:
	pass_chars = pass_chars + random.choice(numbers) + random.choice(numbers)
for x in range(len(pass_chars), num_digits):
	pass_chars = pass_chars + random.choice(upper_case + lower_case)
print(pass_chars)

#Mix up the password
loc = 0
password = ""
loc_set = []
for i in range(0, len(pass_chars)):
	loc = random.choice([i for i in range(0, (len(pass_chars))) if i not in loc_set])
	loc_set.append(loc)
	password = password + pass_chars[loc]


#Output password
print(password)

