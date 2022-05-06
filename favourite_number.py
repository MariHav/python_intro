import json

def get_number_stored():
    """Get the favourite number if already stored"""
    filename = 'favourite_number.json'
    try:
        with open(filename) as f:
            stored_number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return stored_number

def get_newnumber():
    """Ask user to enter his favourite number and save it in json file"""
    new_number = input("\nPlease enter your favourite number: ")
    filename = 'favourite_number.json'
    with open(filename, 'w') as f:
        json.dump(new_number, f)
    return new_number

def print_message():
    """
    Print the message depending on the situation if the programm is opened
    for the first or second time.
    """
    favourite_number = get_number_stored()
    if favourite_number:
        print(f"I know your favourite number! It's {favourite_number}.")
    else:
        favourite_number = get_newnumber()
        print(f"We'll remember your favourite number - {favourite_number}.")

print_message()