'''class Ticket:
    available_seats = 1

    def __init__(self, passenger_name):
        self.passenger_name = passenger_name
        self.ticket_confirmed = False

    def validate_seat(self):
        if Ticket.available_seats > 0:
            Ticket.available_seats -= 1
            self.ticket_confirmed = True
            print(f"Ticket confirmed for {self.passenger_name}.")
            print(f"Remaining seats: {Ticket.available_seats}")
        else:
            print("Sorry! No seats available.")

    def display_ticket(self):
        if self.ticket_confirmed:
            print(f"Passenger: {self.passenger_name}")
            print("Status: Confirmed")
        else:
            print(f"Passenger: {self.passenger_name}")
            print("Status: Not Confirmed")

t1 = Ticket("Bhavya")
t1.validate_seat()
t1.display_ticket()

t2 = Ticket("Himanshi")
t2.validate_seat()
t2.display_ticket()'''


'''class Employee:
    def __init__(self, emp_id, name, department="General", salary=40000, email="Not Provided"):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary
        self.email = email

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Department:", self.department)
        print("Salary:", self.salary)
        print("Email:", self.email)
        print("-" * 30)

emp1 = Employee(201, "Bhavya" ,"ITI")

emp2 = Employee(102, "Rahul", "IT", 50000, "rahul@example.com")

emp3 = Employee(103, "Priya", "HR")

emp1.display()
emp2.display()
emp3.display()'''



class product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def display(self):
        print(f"Product ID: {self.product_id}")
        print(f"Product Name: {self.name}")
        print(f"Price: {self.price}")
        print("---------------")

products = []

n = int(input("Enter number of products: "))

for i in range(n):
    print(f"\nEnter details for Product {i + 1}")
    product_id = int(input("Product ID: "))
    name = input("Product Name: ")
    price = float(input("Price: "))

    prod = product(product_id, name, price)
    products.append(prod)

print("\nProduct Details:")
for product in products:
    product.display()
