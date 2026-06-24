'''class Employee:
    company ="KR Corp"
    _count = 0
    def __init__(self,name,dept):
        self.name =name
        self.dept =dept
        Employee._count += 1
        
        
    @classmethod
    def get_count(bls):
        return f"(bls.company) has (cls._count) employees"
    
    @staticmethod
    def validate_dept(dept):
        valid =["CSE","ECE" ,"MBA","MCA"]
        return dept in valid
    
e1=Employee("Alice" ,"CSE")
e2=Employee("Bob" ,"ECE")
print(Employee.get_count())
 
    
print(Employee.validate_dept("CSE"))   
'''


# Secure student Record 
'''class Student:
    total_students = 0

    def __init__(self, roll_no, marks):
        self.__roll_no = roll_no      
        self._grade = None          
        self.marks = marks            
        self._set_grade()

        Student.total_students += 1

    
    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, marks_list):
        if not isinstance(marks_list, list):
            raise ValueError("Marks must be provided as a list.")

        for mark in marks_list:
            if mark < 0 or mark > 100:
                raise ValueError("Each mark must be between 0 and 100.")

        self.__marks = marks_list

   
    @property
    def gpa(self):
        avg_marks = sum(self.__marks) / len(self.__marks)
        return avg_marks / 10

   
    def _set_grade(self):
        avg = sum(self.__marks) / len(self.__marks)

        if avg >= 90:
            self._grade = "A"
        elif avg >= 75:
            self._grade = "B"
        elif avg >= 60:
            self._grade = "C"
        else:
            self._grade = "D"

   
    @classmethod
    def count(cls):
        return cls.total_students



s1 = Student(2501350086, [85, 80.6,70])
s2 = Student(2501350024, [70, 75, 80])

print("Student 1 GPA:", s1.gpa)
print("Student 2 GPA:", s2.gpa)
print("Total Students:", Student.count())'''


#Library Book Manager
'''class Book:
    def __init__(self, isbn, title, author, copies):
        self.__isbn = isbn         
        self.title = title          
        self._author = author  
        self.__copies = copies     

   
    @property
    def available(self):
        return self.__copies

    
    def checkout(self, n):
        if n <= 0:
            print("Invalid number of copies.")
        elif n > self.__copies:
            print("Not enough copies available.")
        else:
            self.__copies -= n
            print(f"{n} copy/copies checked out successfully.")

    
    def return_book(self, n):
        if n <= 0:
            print("Invalid number of copies.")
        else:
            self.__copies += n
            print(f"{n} copy/copies returned successfully.")



b1 = Book("9780135166307", "Java Programming", "Bhavya ", 10)

print("Available Copies:", b1.available)

b1.checkout(3)
print("Available Copies:", b1.available)

b1.return_book(2)
print("Available Copies:", b1.available)'''


#ATM Machine Simulation
class ATM:
    def __init__(self, pin, balance, owner):
        self.__pin = pin          
        self.__balance = balance  
        self._owner = owner      
    @property
    def balance(self):
        return self.__balance

    
    def authenticate(self, pin):
        return self.__pin == pin

    def deposit_amount(self, amt):
        if amt > 0:
            self.__balance += amt
            print(f"₹{amt} deposited successfully.")
        else:
            print("Invalid amount.")

    
    def withdraw_amount(self, amt):
        if amt > 20000:
            print("Withdrawal limit is ₹20,000 per transaction.")
        elif amt <= 0:
            print("Invalid amount.")
        elif amt > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amt
            print(f"₹{amt} withdrawn successfully.")

    
    def mini_statement(self):
        print("\n----- MINI STATEMENT -----")
        print("Owner   :", self._owner)
        print("Balance :", self.__balance)
        print("--------------------------")



atm = ATM(1234, 50000, "Bhavya")


if atm.authenticate(1234):
    print("Authentication Successful")
else:
    print("Wrong PIN")


atm.deposit_amount(5000)


atm.withdraw_amount(857)


print("Current Balance:", atm.balance)


atm.mini_statement()
