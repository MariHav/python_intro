class User:
    """Create a user profile"""

    def __init__(self, first_name, last_name, age, location):
        self.first = first_name
        self.last = last_name
        self.age = age
        self.location = location

    def describe_user(self):
        user_profile = {}
        user_profile['first_name'] = self.first
        user_profile['last_name'] = self.last
        user_profile['age'] = self.age
        user_profile['location'] = self.location
        print(user_profile)

    def greet_user(self):
        print(f"\nHello, {self.first.title()} {self.last.title()}!")
