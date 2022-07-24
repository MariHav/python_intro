list = ['a','b','c']
indx = 0
val = 'b'

while indx < len(list):
    if list[indx] == val:
        break
    indx += 1
else:
    list.append(val)

print(list)