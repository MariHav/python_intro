def city_country(city,country,population=None):
    """Describe a location"""
    if population:
        world = {'city': city, 'country': country, 'population': population}
    else:
        world = {'city': city, 'country': country}         
    return world

message = city_country('lviv','ukraine',700_000)
print(message)