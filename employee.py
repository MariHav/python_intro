class Employee:
    """Create an employee"""

    def __init__(self,first_name,second_name,salary):
        self.first_name = first_name
        self.second_name = second_name
        self.salary = salary
    
    def give_rise(self,rise = 5000):
        """Calculate the salary tise and returns the final annual salary for an employee"""
        final_salary = int(self.salary) + rise
        return(final_salary)


#new_employee = Employee('Sara','Panero',100000)
#final_amount = new_employee.give_rise()
#print(final_amount)