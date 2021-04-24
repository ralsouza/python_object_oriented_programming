# Python Object-Oriented Programming

class Employee:

    # Constructor
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    emp1 = Employee(first = "Rafael", last = "Lima", pay = 50000)
