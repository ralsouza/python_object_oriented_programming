class Employee:
    """My employee class."""

    # Class variable.
    num_of_emps = 0

    # Instance variable.
    raise_amt = 1.04

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
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp1 = Employee(first="Rafael", last="Lima", pay=50000)
emp2 = Employee(first="Test", last="User", pay=700000)

# Class Methods
# Changing the default value of raise_amt by class method
Employee.set_raise_amt(1.05)

print(Employee.raise_amt)
print(emp1.raise_amt)
print(emp2.raise_amt)

emp_str1 = "Rafael-Lima-50000"
emp_str2 = "User-Test-90000"
emp_str3 = "John-Doe-20000"

new_emp1 = Employee.from_string(emp_str1)

print(new_emp1.email)
print(new_emp1.pay)

# Statics Methods
import datetime

my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))
