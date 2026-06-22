class Dog:
    species ="canine"
    
    def bark(self):
        print("wolf:")
        
dog1 =Dog()
dog2 =Dog()

dog1.bark()        


class LibraryBook:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.avaliable = True
        
    def issue_book(self):
        if self.avaliable:
            self.avaliable=False
            print(f"'{self.title}' is currently unavaliable.")
book1 = LibraryBook("Python Programming","Bhavya","2007")

print("Title:", book1.title)
print("Author:",book1.author)
print("Isbn:",book1.isbn)

book1.issue_book()                

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}")
        print(f"New Balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount}")
            print(f"New Balance: {self.balance}")
        else:
            print("Insufficient balance!")

    def show_balance(self):
        print(f"Current Balance: {self.balance}")

account = BankAccount("Bhavya", 00)

account.show_balance()
account.deposit(2000)
account.withdraw(1500)
account.withdraw(7000)
account.show_balance()