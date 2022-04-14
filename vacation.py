vacation_poll = {}

active = True

while active:
    participants = {}
    name = input("\nPlease enter your name: ")
    place = input("Which place did you visit during your last vacation?: ")
    city = input("Which city would you like to visist?: ")

    participants['place'] = place
    participants['city'] = city

    vacation_poll[name] = participants

    repeat = input("Would you like to let another person respond? (yes/no) ")

    if repeat == 'no':
        active = False

print("\nThank you for taking part in our poll!")
print("The results are the following:")
#print(vacation_poll)
for name, answers in vacation_poll.items():
    print(f"{name.title()}: ")
    for key, value in answers.items():
        print(f"\t{key.title()}: {value.title()}")
