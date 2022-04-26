def profile_builder(first,last,**user_profile):
    """Create a user profile"""
    user_profile['first_name'] = first
    user_profile['last_name'] = last
    return user_profile

my_profile = profile_builder('mariana','sunny',location='lviv',favourite_book=''
'Harry Potter')
print(my_profile)