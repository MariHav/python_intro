drinks = ['wine','scotch','whiskey']
#for drink in drinks:
#    print(f'I like drinking {drink.title()}\n')
#print('However, I prefer drinking water')

friends_drinks = drinks[:]

drinks.append('soda')

friends_drinks.append('martini')

print('My favourite drinks are:')
for drink in drinks:
    print(drink)

print('\nMy friend\'s favourite drinks are:')
for friends_drink in friends_drinks:
    print(friends_drink)