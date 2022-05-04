"""Read from file using 3 possible options"""

"""Option #1"""
filename = 'learning_python.txt'

with open(filename) as file_object:
    contents = file_object.read()

print(contents)

"""Option #2"""
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

"""Option #3"""
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

"""Using replace() function"""
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    line = line.replace('Python','C')
    print(line.rstrip())
