class Employee:
    """My employee class."""

    # Instance variable.
    raise_amt = 1.04

    # This is the constructor.
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@e-mail.com"
        self.pay = pay

    def full_name(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("-->", emp.full_name())


dev1 = Developer(first="Rafael", last="Lima", pay=50000, prog_lang="Python")
dev2 = Developer(first="Test", last="User", pay=700000, prog_lang="Java")

mgr_1 = Manager("Sue", "Smith", 120000, [dev1])

# print(mgr_1.email)
# mgr_1.print_emps()

# print("---- Adding dev2 ----")

# mgr_1.add_emp(dev2)
# mgr_1.print_emps()

# print("---- Removing dev1 ----")
# mgr_1.remove_emp(dev1)
# mgr_1.print_emps()

# print(dev1.email)
# print(dev1.prog_lang)

# print(dev1.pay)
# dev1.apply_raise()
# print(dev1.pay)

# isinstance()
print("--> Is mgr_1 a instance of Manager class?")
print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))

# issubclass()
print("--> Is Developer a subclass of Employee?")
print(issubclass(Developer, Employee))
print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))