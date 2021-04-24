# Python Object-Oriented Programming

# Class Creation
class Employee:
    """My employee class."""

    # This is the constructor.
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def full_name(self):
        return "{} {}".format(self.first, self.last)


# Class Instantiation
emp1 = Employee(first="Rafael", last="Lima", pay=50000)
emp2 = Employee(first="Test", last="User", pay=700000)

# Get e-mail addresses
print(emp1.email)
print(emp2.email)

# Print first and last names
# print("{} {}".format(emp1.first, emp1.last))

# Print full name calling the class method
print(emp1.full_name())
print(emp2.full_name())

# Another way to use a class method
print(Employee.full_name(emp1))
