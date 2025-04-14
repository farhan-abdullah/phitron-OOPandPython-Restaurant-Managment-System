from foodItem import FoodItem
from Menu import Menu
from Users import Customer, Admin, Employee
from Restaurant import Restaurant
from Orders import Order
mamar_restaurant = Restaurant('Mamar Restaurant')
def customer_menu():
    name = input('Enter Your Name: ')
    email = input('Enter Your email: ')
    phone = input('Enter Your phone: ')
    address = input('Enter Your address: ')
    customer = Customer(name=name,email=email,phone=phone, address=address)
    
    while True:
        print(f'Welcome {customer.name}!!!')
        print('1. View Menu')
        print('2. Add item to cart')
        print('3. View cart')
        print('4. PayBill')
        print('5. Exit')
        
        choice = int(input('Enter Your Choice: '))
        if choice == 1:
            customer.view_menu(mamar_restaurant)
        elif choice == 2:
            item_name = input('Enter item name: ')
            item_quantity = int(input('Enter item quantity: '))
            customer.add_to_cart(mamar_restaurant,item_name,item_quantity)
            
        elif choice == 3:
             customer.view_cart()
        elif choice == 4:
             customer.pay_bill()
        elif choice == 5:
            break
        else:
            print('Invalid input!!!')   
            
def admin_menu():
    name = input('Enter Your Name: ')
    email = input('Enter Your email: ')
    phone = input('Enter Your phone: ')
    address = input('Enter Your address: ')
    admin = Admin(name=name,email=email,phone=phone, address=address)
    
    while True:
        print(f'Welcome {admin.name}!!!')
        print('1. Add new Item')
        print('2. Add new employee')
        print('3. View employee')
        print('4. view items')
        print('5. Delete items')
        print('6. Exit')
        
        choice = int(input('Enter Your Choice: '))
        if choice == 1:
            item_name = input('Enter item name: ')
            item_price = int(input('Enter item price: '))
            item_quantity = int(input('Enter item quantity: '))
            item = FoodItem(item_name,item_price,item_quantity)
            admin.add_new_item(mamar_restaurant,item)
        elif choice == 2:
            name = input('Enter employee Name: ')
            email = input('Enter employee email: ')
            phone = input('Enter employee phone: ')
            designation = input('Enter employee designation: ')
            age = input('Enter employee age: ')
            salary = input('Enter employee salary: ')
            address = input('Enter employee address: ')
            employee = Employee(name,email,phone,address,age,designation,salary)
            admin.add_employee(mamar_restaurant,employee)
            
            
        elif choice == 3:
             admin.view_employee(mamar_restaurant)
        elif choice == 4:
             admin.view_menu(mamar_restaurant)
        elif choice == 5:
            item = input('Enter item name: ')
            admin.remove_item(mamar_restaurant, item)
        elif choice == 6:
            break
        else:
            print('Invalid input!!!')   


while True:
    print('Welcome!')
    print('1. Customer!')
    print('2. Admin!')
    print('3. Exit!')
    
    choice = int(input('Enter your choice: '))
    if choice == 1:
        customer_menu()
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        break
    else:
        print('Wrong choice, try again!')