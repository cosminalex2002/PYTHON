class Employee:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    def print_info(self):
        return f"Employee ID: {self.id}\nName: {self.name}\nSalary: {self.salary} lei"


class Manager(Employee):

    def __init__(self, name, id, salary, department):
        super().__init__(name, id, salary)
        self.department = department

    def print_info(self):
        return super().print_info() + f"\nDepartment: {self.department}"


class Engineer(Employee):
    def __init__(self, name, id, salary, programming_language):
        super().__init__(name, id, salary)
        self.programming_language = programming_language

    def print_info(self):
        return super().print_info() + f"\n Language: {self.programming_language}"


class Salesperson(Employee):
    def __init__(self, name, id, salary, sales_target):
        super().__init__(name, id, salary)
        self.sales_target = sales_target

    def print_info(self):
        return super().print_info() + f"\nSales Target: {self.sales_target} lei"




manager = Manager(name="Costel", id=1, salary=6000, department="HR")
print(manager.print_info())

engineer = Engineer(name="Ionel", id=2, salary=7000, programming_language="Python")
print(engineer.print_info())


