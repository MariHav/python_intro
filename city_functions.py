def get_city_country(city,country,population=''):
    """Generate formatted city and its country"""
    get_population = f' - population {population}'
    formatted_city_country = f'{city.title()}, {country.title()}'

    if population:
        return formatted_city_country+get_population
    else:
        return formatted_city_country

    