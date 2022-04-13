favourite_numbers = {
    'serik': [25, 3, 11],
    'mariana': [11, 7],
    'oksana': [21, 12],
    'olha': [5, 10, 8]
}

#print(f"Serik\'s favourite_number is {favourite_numbers['serik']}")
#print(f"Mariana\'s favourite number is {favourite_numbers['mariana']}")
#print(f"Oksana\'s favourite number is {favourite_numbers['oksana']}")
#print(f"Olha\'s favourite number is {favourite_numbers['olha']}")

#for name, number in sorted(favourite_numbers.items()):
#    print(f"{name.title()}'s favourite number is {number}\n")

#names = ['serik','mariana','oksana','olha','julia','olena']

#for name in names:
    #if name in favourite_numbers.keys():
        #print(f'{name.title()}, thank you for taking part in voting')
    #else:
        #print(f'{name.title()}, we would be glad if you take part in our voting.')

for name, numbers in favourite_numbers.items():
    print(f'\n{name.title()}: ')
    for number in numbers:
        print(number)
