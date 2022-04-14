question = "\nPlease kindly provide your age: "

active = True

while active:
    age = input(question)

    if age == 'quit':
        active = False
    else:
        age = int(age)

        if age < 3:
            print("\nThe ticket is free.")
        elif age < 12:
            print("\nThe cost of the ticket is 10%.")
        else:
            print("\nThe cost of the ticket is 15%.")