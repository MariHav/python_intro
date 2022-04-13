magicians = ['alice','david','carolina','jane','amanda']
#for magician in magicians:
#    print(f'{magician.title()}, that was a great trick!')
#    print(f'I can\'t wait to see your next trick, {magician.title()}.\n')
#print('Thank you, everyone. It was a great magic show!')

print('The firts three name in the list are:')
for magician in magicians[:3]:
    print(magician)
print('The names from the middle of the list are:')
for magician in magicians[1:4]:
    print(magician)
print('The last three names in the list are:')
for magician in magicians[-3:]:
    print(magician)