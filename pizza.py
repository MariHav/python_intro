pizza = "\nPlease enter the ingredient for your pizza."
pizza += "\nEnter 'quit' when you are finished. "

message = ""

while message != 'quit':
    message = input(pizza)

    if message != 'quit':
        print(f"\nAdding {message} to your pizza.")