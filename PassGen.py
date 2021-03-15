import random
import sys

def instructions():
	print("Welcome to PassGen!")
	print("To use PassGen enter values for three arguments.")
	print("Argument 1: Password Length (int)")
	print("Argument 2: Include Numbers (0=N or 1=Y)")
	print("Argument 3: Include Special Characters (0=N or 1=Y)")
	return

#Take system arguments and validate to determine if special/numbers are used and length of password
if (len(sys.argv) != 4):
	print("ERROR! Incorrect number of arguments entered.")
	instructions()
	sys.exit(0)
set_bools = [0,0]
try:
	num_digits = int(sys.argv[1])
	set_bools[0] = int(sys.argv[2])
	set_bools[1] = int(sys.argv[3])
	
except ValueError:
	print("Error: Incorrect arguments entered.")
	instructions()
	sys.exit(0)

#Take requirements in upper case, lower case, special chars, numbers, etc
numbers = "0123456789"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case = "abcdefghijklmnopqrstuvwxyz"
special = "!#$%&()+<=>?@^~"

#Get characters for the password
pass_chars = ""
if set_bools[1] == 1:
	pass_chars = pass_chars + random.choice(special) + random.choice(special)
if set_bools[0] == 1:
	pass_chars = pass_chars + random.choice(numbers) + random.choice(numbers)
for x in range(len(pass_chars), num_digits):
	pass_chars = pass_chars + random.choice(upper_case + lower_case)

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

