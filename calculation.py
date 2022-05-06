print("Give me two numbers and I will add them.")
print("Enter 'q' to quit.")

while True:

    first_number = input("Enter firts number: ")
    if first_number == 'q':
        break

    second_number = input("Enter second number: ")
    if second_number == 'q':
        break

    try:
        calculation = int(first_number)+int(second_number)
        print(calculation)
    except ValueError:
        print("Please enter only numbers!")
    
