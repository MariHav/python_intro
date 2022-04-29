from random import choice

lottery = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e']

lucky_ticket = []

count = 0

while count < 4:
    number = choice(lottery)
    lucky_ticket.append(number)
    count = count+1

print("\nThe lucky ticket number is:")
print(lucky_ticket)
