from random import choice

lottery = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e']

my_ticket = [1, 9, 'd', 2]

lucky_ticket = []

loop = 0

while True:

    lucky_ticket = [choice(lottery), choice(lottery), choice(lottery), 
    choice(lottery)]
    """
    count = 0

    while count < 4:
        number = choice(lottery)
        lucky_ticket.append(number)
        count = count+1
    """
    if my_ticket != lucky_ticket:
        loop = loop+1
        continue
    else:
        break    

print("Congrats! You won!")
print(lucky_ticket)
print(loop)  


  
