from Menu import Menu
class Restaurant:
    def __init__(self, name):
        self.name = name
        self.employees = []
        self.menu = Menu()# ai khane Menu fooditem er ekta object
    def add_employee(self,employee):
         self.employees.append(employee)
    def view_employee(self):
        print('Employee List!!!')
        for emp in self.employees:
            print(emp.name, emp.email, emp.phone, emp.address)
