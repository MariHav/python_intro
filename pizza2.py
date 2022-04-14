pizza = "\nPlease enter the ingredient for your pizza."
pizza += "\nEnter 'quit' when you are finished. "

while True:
    message = input(pizza)

    if message == "quit":
        break
    else:
        print(f"\nAdding {message} to your pizza.")