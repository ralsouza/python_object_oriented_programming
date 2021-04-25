class Employee:
    """My employee class."""

    # Instance variable.
    raise_amt = 1.04

    # This is the constructor.
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def full_name(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


emp1 = Employee(first="Rafael", last="Lima", pay=50000)
emp2 = Employee(first="Test", last="User", pay=700000)