names = ['Mariana','Olha','Julia']
#print(names)
#invitation1 = f'Dear {names[0]}, I am glad to invite you to the best party in the world'
#invitation2 = f'Dear {names[1]}, I am glad to invite you to the best party in the world'
#invitation3 = f'Dear {names[-1]}, I am glad to invite you to the best party in the world'
#
#print(invitation1)
#print(invitation2)
#print(invitation3)

missed_guest = 'Olha'
names.remove('Olha')

names.insert(1,'Olena')

#print(names)
#invitation1 = f'Dear {names[0]}, I am glad to invite you to the best party in the world'
#invitation2 = f'Dear {names[1]}, I am glad to invite you to the best party in the world'
#invitation3 = f'Dear {names[-1]}, I am glad to invite you to the best party in the world'
#
#print(missed_guest)
#print(invitation1)
#print(invitation2)
#print(invitation3)

#print('Dear guests, I have found a bigger table for our party')
names.insert(0,'Serik')
names.insert(2,'Marko')
names.append('Liliia')

print(names)

invitation1 = f'Dear {names[0]}, I am glad to invite you to the best party in the world'
invitation2 = f'Dear {names[1]}, I am glad to invite you to the best party in the world'
invitation3 = f'Dear {names[2]}, I am glad to invite you to the best party in the world'
invitation4 = f'Dear {names[3]}, I am glad to invite you to the best party in the world'
invitation5 = f'Dear {names[4]}, I am glad to invite you to the best party in the world'
invitation6 = f'Dear {names[-1]}, I am glad to invite you to the best party in the world'

#print(invitation1)
#print(invitation2)
#print(invitation3)
#print(invitation4)
#print(invitation5)
#print(invitation6)

print('I am sorry, but I can invite only two people:(')

firts_popped = names.pop()
print(f'Sorry, {firts_popped}, but I cannot invite you to my party')

second_popped= names.pop(0)
print(f'Sorry, {second_popped}, but I cannot invite you to my party')

third_popped = names.pop(-1)
print(f'Sorry, {third_popped}, but I cannot invite you to my party')

forth_popped = names.pop(1)
print(f'Sorry, {forth_popped}, but I cannot invite you to my party')


print(f'Dear {names[0]}, I am happy to inform you that you are still in the guest list')
print(f'Dear {names[1]}, I am happy to inform you that you are still in the guest list')

del names[0]
del names[0]
print(names)