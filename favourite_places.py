favourite_places = {
    'serik': ['barcelona','amsterdam','lviv'],
    'mariana': ['london','lviv','kyiv'],
    'oksana': ['rome','odessa','krakiv']
}

for name, places in favourite_places.items():
    print(f'\n{name.title()}\'s favourite palces are:')
    for place in sorted(places):
        print(f'\t{place.title()}')