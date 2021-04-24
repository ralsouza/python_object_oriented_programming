class Employee:
    """My employee class."""

    # Class variable.
    num_of_emps = 0

    # Instance variable.
    raise_amount = 1.04

    # This is the constructor.
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emps += 1

    def full_name(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


print(Employee.__dict__)

print(Employee.num_of_emps)

emp1 = Employee(first="Rafael", last="Lima", pay=50000)
emp2 = Employee(first="Test", last="User", pay=700000)

emp1.raise_amount = 1.05

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

print(Employee.num_of_emps)
