def city_country(city,country):
    location = {'city': city, 'country': country}
    return location

while True:
    print("\nPlease tell me your location.")
    print("You can type quit to exit.")

    yourcity = input("Please tell me your city: ")
    if yourcity == 'quit':
        break

    yourcountry = input("Please tell me your country ")
    if yourcountry == 'quit':
        break
    
    your_location = city_country(yourcity,yourcountry)
    print(your_location)