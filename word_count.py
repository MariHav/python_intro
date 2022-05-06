def word_count(filename):
    """Count the number of word 'the' in the text file"""
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        number = contents.lower().count('the ')
        print(f"\nThe file {filename} has about {number} occurence of the word "
        +"'the'.")

filenames = ['alice.txt','little_women.txt','moby_dick.txt']
for filename in filenames:
    word_count(filename)
