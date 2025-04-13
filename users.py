from abc import ABC

class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        

class Employee(User):
    def __init__(self, name, phone, email, address,age, designation, salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary



class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.employees = [] # eta amader data base

    def add_employee(self,restaurant,employee):
        restaurant.add_employee(employee)

    def view_employee(self, restaurant):
        restaurant.view_employee()

    def add_new_item(self, restaurant,item):
        restaurant.menu.add_menu_item(item)

    def delete_item(self, restaurant,item):
        restaurant.menu.remove_item(item)

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.employees = []
        self.menu = FoodItem()# ai khane Menu fooditem er ekta object
    def add_employee(self,employee):
         self.employees.append(employee)
    def view_employee(self):
        print('Employee List!!!')
        for emp in self.employees:
            print(emp.name, emp.email, emp.phone, emp.address)

class Menu:
    def __init__(self):
        self.items = []
    def add_menu_item(self,item):
        self.items.append(item)
    def find_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None
    def remove_item(self,item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print('Item deleted')
        else:
            print('Item not found')
    def show_menu(self):
        print('******Menu*******')
        print('Name\tprice\tQuantity')
        for item in self.items:
            print(f'{item.name}\t{item.price}\t{item.quantity}')

class FoodItem:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity





        
# Sample data
admin = Admin("Admin User", "1234567890", "admin@example.com", "123 Admin Street")
restaurant = Restaurant("Tasty Bites")

# Add employee
emp1 = Employee("John Doe", "0987654321", "john@example.com", "456 Employee Ave", 30, "Chef", 5000)
admin.add_employee(restaurant, emp1)

# View employees
admin.view_employee(restaurant)

mn = Menu()
item = FoodItem('Pizza', 1600, 10)

mn.add_menu_item(item)
mn.show_menu()