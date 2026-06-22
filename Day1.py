'''a="Hello World "
print(a)

print("Hello World !")
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

operator = input("Enter operator (+, -, *, /,%,**): ")

if operator == "+":
    print("Result:", a + b)
elif operator == "-":
    print("Result:", a - b)
elif operator == "*":
    print("Result:", a * b)
elif operator == "/":
    if b == 0:
        print("Error! Division by zero.")
    else:
        print("Result:", a / b)
elif operator == "%":
    print("Result:", a % b)       
        
elif operator == "**":
    print("Result:", a ** b)          
else:
    print("Invalid operator")'''
    

'''a = int(input("Enter the number of employee : "))
for i in range (0 ,a+1) :
    id = int(input("Enter employee id : "))
    name = input("Enter employee name : ")
    salary = int(input("Enter employee salary : "))
    
    hra = salary/100 *20 
    da = salary/100 * 15
    ta = salary/100 * 10
    print("HRA : ",hra)
    print("DA : ",da)
    print("TA : ",ta)
    gross_salary = salary + hra + da + ta
    print("Gross Salary : ",gross_salary)  '''
    


#create a atm machine program
balance = 1000  
while True:
    print("Welcome to the ATM Machine!")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transaction History")
    print("5. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        print(f"Your current balance is: ${balance}")
        
    elif choice == '2':
        amount = float(input("Enter the amount to deposit: "))
        if amount > 0:
            balance += amount
            print(f"${amount} deposited successfully. New balance: ${balance}")
        else:
            print("Invalid amount. Please enter a positive number.")
            
    elif choice == '3':
        amount = float(input("Enter the amount to withdraw: "))
        if amount > balance:
            print("Insufficient funds. Please try again.")
        elif amount <= 0:
            print("Invalid amount. Please enter a positive number.")
        else:
            balance -= amount
            print(f"${amount} withdrawn successfully. New balance: ${balance}")
            
    elif choice == '4':
        print("Transaction history feature is currently unavailable. Please check back later.")        
            
    elif choice == '5':
        print("Thank you for using the ATM Machine. Goodbye!")
        break
        
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
        
        