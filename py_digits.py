filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your B-day, in the form mmddyy: ")
if birthday in pi_string:
    print("Your B-day appears in the first million digits of pi!")
else:
    print("Your B-day does not appear in the first million digits of pi!")