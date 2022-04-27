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

user_1 = User('mariana', 'sunny', 31, 'lviv')
user_2 = User('serik', 'sunny', 34, 'kyiv')
user_3 = User('olenka', 'bilchenia', 31, 'odessa')

#user_1.describe_user()
#user_2.describe_user()
#user_3.describe_user()
#user_1.greet_user()
#user_2.greet_user()
#user_3.greet_user()

class Privileges:
    """Define privileges of an admin user"""

    def __init__(self, privileges = ['can add post','can delete post',
    'can ban user']):
        self.privileges = privileges

    def show_privileges(self):
        print("Admin has the following privileges:")
        for privilige in self.privileges:
            print(privilige)

class Admin(User):
    """Describe an admin user with the special rights"""

    def __init__(self, first_name, last_name, age, location):
        super().__init__(first_name, last_name, age, location)
        self.privileges = Privileges()

new_admin = Admin('Mariana', 'Sunny', 31, 'Lviv')
new_admin.privileges.show_privileges()