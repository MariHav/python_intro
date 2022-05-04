message = input("\nPlease enter your name if you are going to attend the party "
+ "or quit if not: ")
filename = 'guests.txt'

with open(filename, 'a') as file_object:
    file_object.write(message)

