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

    def __repr__(self):
        """A string to recreate an object."""
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        """Return the full name and e-mail."""
        return "{} - {}".format(self.full_name(), self.email)

    def __add__(self, other):
        """Combine salaries of two employees, if comment this method an error will occur."""
        return self.pay + other.pay

    def __len__(self):
        """Return count of full name."""
        return len(self.full_name())


emp1 = Employee(first="Rafael", last="Lima", pay=50000)
emp2 = Employee(first="Test", last="User", pay=60000)

print(emp1 + emp2)

print(emp1)

print(emp1.__repr__())
print(emp1.__str__())

print(1+2)
print(int.__add__(1,2))
print(str.__add__("a", "b"))

print(len("test"))
print("test".__len__())
print(len(emp1))