cities = {
    'lviv': {
        'country': 'ukraine',
        'population': 1_000_000,
        'established': 1256
        },
    'kyiv': {
        'country': 'ukraine',
        'population': 5_000_000,
        'established': 887
        },
    'odessa': {
        'country': 'ukraine',
        'population': 3_000_000,
        'established': 791
        }
    }

for city, infos in sorted(cities.items()):
    print(f'\n{city.title()}')
    for key, value in infos.items():
        print(f'\t{key}: {value}')