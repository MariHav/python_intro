sandwiches_ordered = ['sandwich with cheese', 'pastrami sandwich''sandwich with '
+'salmon','sandwich with chicken and tomatos', 'sandwich with avocado', 
'pastrami sandwich', 'pastrami sandwich']

sandwiches_finished = []

print('\nPlease note that we are lack of pastrami.')

while 'pastrami sandwich' in sandwiches_ordered:
    sandwiches_ordered.remove('pastrami sandwich')

while sandwiches_ordered:
    sandwich_finished = sandwiches_ordered.pop()
    print(f"\nI have made your {sandwich_finished}.")

    sandwiches_finished.append(sandwich_finished)

print("\nI have made the following sandwiches:")
for sandwich in sandwiches_finished:
    print(sandwich)