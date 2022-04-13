my_friend_0 = {
    'first_name': 'serik',
    'last_name': 'pietinov',
    'age': 30,
    'city': 'Barcelona'
    }

my_friend_1 = {
    'first_name': 'olenka',
    'last_name': 'topalova',
    'age': 30,
    'city': 'london'
}

my_friend_2 = {
    'first_name': 'olha',
    'last_name': 'bosiak',
    'age': 30,
    'city': 'kyiv'
}

my_friends = [my_friend_0, my_friend_1, my_friend_2]

for friend in my_friends:
    for key, value in friend.items():
        if key == 'age':
            print(f"{key}: {value}")
        else:
            print(f"{key}: {value.title()}")

