pizza = "\nPlease enter the ingredient for your pizza."
pizza += "\nEnter 'quit' when you are finished. "

active = True

while active:
    message = input(pizza)
    if message == 'quit':
        active = False
    else:
        print(f"\nAdding {message} to your pizza.")