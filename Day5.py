# Library Fine Calculator for multiple students


'''def calculate_fine(delay: int) -> int:
    if delay <= 0:
        return 0
    elif delay <= 5:
        return delay * 5
    elif delay <= 10:
        return delay * 10
    else:
        return delay * 20


students = {}

n = int(input("Enter number of students: "))

for _ in range(n):
    name = input("\nEnter student name: ")
    books = int(input(f"How many books did {name} return? "))
    fines = []

    for i in range(books):
        due = int(input(f"  Book {i + 1} due day: "))
        ret = int(input(f"  Book {i + 1} return day: "))
        delay = ret - due
        fine = calculate_fine(delay)
        fines.append(fine)

    students[name] = fines


print("\n===== Fine Report ====")

total_fines = []
for name, fines in students.items():
    total = sum(fines)
    total_fines.append(total)

    print(f"\nStudent: {name}")
    for i, fine in enumerate(fines, start=1):
        print(f"  Book {i}: Fine = ₹{fine}")

    print(f" Total Fine = ₹{total}")


print("\n===== Summary =====")
print(f"Highest Fine = ₹{max(total_fines)}")
print(f"Average Fine = ₹{sum(total_fines) / len(total_fines):.2f}")'''




#LAB EXERCISE (Function , Recursion , Pass -by-Value ,Function as Variable )


def student_report(name, marks):
    print("\n----- Student Report -----")
    print(f"Name : {name}")
    print(f"Marks : {marks}")
    print("--------------------------")

def add_bonus(marks):
    marks_bonus = marks + 5
    print(f"\nInside Function Marks  : {marks_bonus}")
    return marks_bonus

def sum_of_marks(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return n + sum_of_marks(n - 1)

def square(x):
    return x * x

def cube(x):
    return x ** 3

def apply_operation(func, value):
    return func(value)

def main():
    
    name = input("Enter Student Name: ").strip()
    while True:
        try:
            marks = int(input("Enter Marks: ").strip())
            break
        except ValueError:
            print("Please enter an integer for marks.")

    student_report(name, marks)

  
    inside_marks = add_bonus(marks)  
    print(f"Outside Function Marks : {marks}")  
   
    while True:
        try:
            n = int(input("\nEnter a number for recursive sum: ").strip())
            if n < 0:
                print("Please enter a non-negative integer.")
                continue
            break
        except ValueError:
            print("Please enter an integer.")
    rec_sum = sum_of_marks(n)
    print(f"Recursive Sum = {rec_sum}")

    print("\nChoose Operation:")
    print("1. Square")
    print("2. Cube")

    while True:
        choice = input("Enter Choice (1 or 2): ").strip()
        if choice not in ("1", "2"):
            print("Invalid choice. Enter 1 or 2.")
            continue
        try:
            number = float(input("Enter Number: ").strip())
        except ValueError:
            print("Please enter a valid number.")
            continue
        if choice == "1":
            func = square
        else:
            func = cube

        result = apply_operation(func, number)
        
        if result.is_integer():
            result = int(result)
        print(f"Result = {result}")
        break

if __name__ == "__main__":
    main()


'''for item in [1,2,3]:
    print(item)
    
    
    
list1=[1,2]
list2=[4,5]

a = list1+list2
print(a)


for i in [10, 20]:   
    for j in [1, 2]:    
        print(i, j)     

for i in range(1, 11):   
    print(2 * i)

for i in range(2, 3):        
    for j in range (1, 11):   
        print(i, "x", j, "=", i * j)
        
for i in range(3, 6):        
    for j in range (1, 11):   
        print(i, "x", j, "=", i * j)        



for i in range (2,4):
    for j in range(1,11):
       

        print("i =", i, "j =", j)  
        if i == j:                
          
            break                  


for i in range(2, 4):             
    for j in range(1, 11):        
        if i == j:                
            continue               
        print("i =", i, "j =", j) 
        

b = [5, 12, 7, 18, 3, 20]
val = [x for x in b if x > 10]
print(val)

a=[i for i in range(10)]
print(a)
        
# Printing the pattern
for i in range(1, 9):
         
    print("*" * i)      
    
'''
      