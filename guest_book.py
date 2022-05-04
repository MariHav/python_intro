question = "\nPlease enter your name or quit: "

while True:
    message = input(question)
    
    if message != 'quit':
        print(f"Hello, {message.title()}!")
        
        filename = 'guest_book.txt'
        with open(filename, 'a') as file_object:
            file_object.write(f"\n{message.title()}")
    else:
        break