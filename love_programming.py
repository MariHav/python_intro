question = "\nWhy do you like programming?:"
question += "\nYou can enter quit to exit the program. "

while True:
    message = input(question)

    if message != 'quit':
        print('Thnak you for your answer!')
        filename = 'love_programming.txt'
        with open(filename, 'a') as file_object:
            file_object.write(f"{message}\n")
    else:
        break