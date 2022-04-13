capitals = {
    'ukraine': 'kyiv',
    'great britain': 'london',
    'france': 'paris'
    }
#for country, capital in capitals.items():
#    print(f'{capital.title()} is the capital of {country.title()}.\n')

#for capital in sorted(capitals.values()):
#    print(capital.upper())

for country in capitals.keys():
    print(country.title())