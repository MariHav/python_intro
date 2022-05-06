def print_contents(filename):
    """Print the content of the file"""
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        print(contents)

filenames = ['Cats.txt','Dogs.txt']
for filename in filenames:
    print_contents(filename)
