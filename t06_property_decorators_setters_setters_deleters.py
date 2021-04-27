class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return "{}.{}@company.com".format(self.first, self.last)

    @property
    def full_name(self):
        return "{} {}".format(self.first, self.last)

    # Setter to change the full name
    @full_name.setter
    def full_name(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @full_name.deleter
    def full_name(self):
        self.first = None
        self.last = None
        print("Name has deleted!")


emp_1 = Employee(first="Rafael", last="Lima")

# Changing the emp_1 name
emp_1.full_name = "Cristiane Hernandes"

print(emp_1.first)
print(emp_1.email)
print(emp_1.full_name)

del emp_1.full_name