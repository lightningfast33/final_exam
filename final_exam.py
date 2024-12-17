"Final Exam"
class Customer:
    def __init__(self,name,email,address):
        self.name=name
        self.email=email
        self.address=address
        self.balance=0.0
        self.past_orders=[]

    def add_funds(self,amount):
        self.balance+=amount

    def check_balance(self):
        return self.balance

    def view_menu(self,menu):
        menu_items=[]
        for item in menu:
            menu_items.append(str(item))
        return "\n".join(menu_items)

    def place_order(self,menu,item_name):
        for item in menu:
            if item.name.lower()==item_name.lower():
                if self.balance>=item.price:
                    self.balance-=item.price
                    self.past_orders.append(item.name)
                    return f"Order placed:{item.name}.Remaining balance:${self.balance:.2f}"
                else:
                    return "Insufficient balance.Please add funds."
        return "Item not found on the menu."

    def view_past_orders(self):
        if self.past_orders:
            return "\n".join(self.past_orders)
        else:
            return "No past orders found."

class Admin:
    def __init__(self):
        self.menu=[]
        self.customers=[]

    def add_menu_item(self,name,price):
        self.menu.append(MenuItem(name,price))

    def remove_menu_item(self,name):
        for item in self.menu:
            if item.name.lower()==name.lower():
                self.menu.remove(item)
                return

    def view_menu(self):
        menu_items=[]
        for item in self.menu:
            menu_items.append(str(item))
        return "\n".join(menu_items)

    def update_menu_item(self,name,new_price):
        for item in self.menu:
            if item.name.lower()==name.lower():
                item.price=new_price
                return

    def add_customer(self,name,email,address):
        self.customers.append(Customer(name,email,address))

    def remove_customer(self,email):
        for customer in self.customers:
            if customer.email.lower()==email.lower():
                self.customers.remove(customer)
                return

    def view_customers(self):
        customer_list=[]
        for customer in self.customers:
            customer_list.append(f"{customer.name} (Email: {customer.email})")
        return "\n".join(customer_list)
    
class MenuItem:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def __str__(self):
        return f"{self.name}:${self.price:.2f}"
    
class Restaurant:
    def __init__(self):
        self.admin=Admin()

    def get_menu(self):
        return self.admin.menu

    def get_customers(self):
        return self.admin.customers

def main():
    restaurant=Restaurant()
    admin=restaurant.admin

    while True:
        print("\n___ Restaurant Management System ___")
        print("1. Admin Login")
        print("2. Customer Login")
        print("3. Exit")
        choice=input("Choose an option: ")

        if choice=="1":
            while True:
                print("\n___ Admin Menu ___")
                print("1. View Menu")
                print("2. Add Menu Item")
                print("3. Remove Menu Item")
                print("4. Update Menu Item")
                print("5. View Customers")
                print("6. Add Customer")
                print("7. Remove Customer")
                print("8. Logout")
                admin_choice=input("Choose an option: ")

                if admin_choice=="1":
                    print(admin.view_menu())

                elif admin_choice=="2":
                    name=input("Enter the menu item name: ")
                    price=float(input("Enter the price: "))
                    admin.add_menu_item(name,price)

                elif admin_choice=="3":
                    name=input("Enter the menu item name to remove: ")
                    admin.remove_menu_item(name)

                elif admin_choice=="4":
                    name=input("Enter the menu item name to update: ")
                    new_price=float(input("Enter the new price: "))
                    admin.update_menu_item(name,new_price)

                elif admin_choice=="5":
                    print(admin.view_customers())

                elif admin_choice=="6":
                    name=input("Enter customer name: ")
                    email=input("Enter customer email: ")
                    address=input("Enter customer address: ")
                    admin.add_customer(name,email,address)

                elif admin_choice=="7":
                    email=input("Enter the email of the customer to remove: ")
                    admin.remove_customer(email)

                elif admin_choice=="8":
                    break
                else:
                    print("Invalid option.Please try again.")

        elif choice=="2":
            email=input("Enter your email: ")
            found_customer=None
            for customer in admin.customers:
                if customer.email.lower()==email.lower():
                    found_customer=customer
                    break

            if found_customer:
                customer=found_customer
                while True:
                    print("\n___ Customer Menu ___")
                    print("1. View Menu")
                    print("2. Place an Order")
                    print("3. Check Balance")
                    print("4. Add Funds")
                    print("5. View Past Orders")
                    print("6. Logout")
                    customer_choice=input("Choose an option: ")

                    if customer_choice=="1":
                        print(customer.view_menu(admin.menu))

                    elif customer_choice=="2":
                        item_name=input("Enter the menu item to order: ")
                        print(customer.place_order(admin.menu,item_name))

                    elif customer_choice=="3":
                        print(f"Your current balance is: ${customer.check_balance():.2f}")

                    elif customer_choice=="4":
                        amount=float(input("Enter amount to add: "))
                        customer.add_funds(amount)
                        print(f"Added ${amount:.2f} to your balance.")

                    elif customer_choice=="5":
                        print(customer.view_past_orders())

                    elif customer_choice=="6":
                        break
                    else:
                        print("Invalid option.Please try again.")
            else:
                print("Customer not found.")

        elif choice=="3":
            print("Bye bye")
            break

        else:
            print("Invalid option.Please try again.")


if __name__=="__main__":
    main()
