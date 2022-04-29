
from class_user import User

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
