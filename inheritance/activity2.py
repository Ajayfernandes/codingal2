class Person:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number
    def display(self):
        print(self.name)
        print(self.id_number)

class Employee(Person):
    def __init__(self, name, id_number, salary, post):
        self.salary = salary
        self.post = post
        Person.__init__(self, name, id_number)
obj = Employee("ajay", "9235k", 20000, "intern")
obj.display()


