'''x=30
y=10
if x<y :
    print("x is smaller  than y ")
else:
    print("Meauuuuuuuuuuu")'''
    

#Find the maximum among two number 
'''a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

if a > b:
    print("Maximum is:", a)
else:
    print("Maximum is:", b)'''
    
    
# Input a number (N) and adds 7to N if N is odd Else add 4  

'''N = int(input("Enter a number: "))

if N % 2 != 0:   
    result = N + 7
else:           
    result = N + 4

print("Result:", result) '''



# Rolled with concept of python 
'''import random

dice = random.randint(1, 6)

guess = int(input("Enter your guess (1-6): "))

if guess == dice:
    print(" Congratulations! You guessed it right.")
else:
    print(" Sorry! The dice was:", dice)'''
 
 #Check number is positive or negative   
'''number = int(input("Enter the number : "))
if number>=0:
    if number== 0:
        print("Number is 0")
    else:
        print("Number is positive ") 
else:
        print("Number is negative")'''
        
        
# Find Maximum            
'''a=int(input("Enter a number of a :"))  
b=int(input("Enter a number of b :"))    
c=int(input("Enter a number of c :"))      
if (a>b) :
    if (a>c):
        print("a is max")
    else:
        print("c is max") 
else:
        if (b>c):
            print("b is max")
        else:
            print("c is max")'''
            
       
       
# Check positive negative or zero then if positive check even or odd
'''number = int(input("Enter the number : "))
if number>=0:
        print("Number is positive ") 
        if number % 2==0:
            print ("Number is even ")
        else:
            print ("Number is odd ")
            
if number== 0:
        print("Number is 0")
        if number<0:
            
           print("Number is negative")'''
           
           
#  3 Inputs and check which greater      
'''a=int(input("Enter a number of a :"))  
b=int(input("Enter a number of b :"))    
c=int(input("Enter a number of c :"))      
if (a>b) :
    if (a>c):
        print("a is max")
    else:
        print("c is max") 
else:
        if (b>c):
            print("b is max")
        else:
            print("c is max")         '''
            
            
            
            
#Calculate the Grade of a student 

'''Grade = float(input("Enter the Grade of Student : "))
if 90 <= Grade <= 100:
    print("Score A Grade")
elif 80 <= Grade < 90:
    print("Score B Grade")
elif 70 <= Grade < 80:
    print("Score C Grade")
elif 60 <= Grade < 70:
    print("Score D Grade")
else:
    print("Fail")'''
    
#Check if a year entered by the user is a leap year or not.and a leap year if it is divisible by 4 but not by 100, unless if it is also divisible by 400. pint appropriate message to the user.
'''print("---------------------------------------------------")
print("Welcome to the Leap Year Checker")
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
print("---------------------------------------------------")    '''


#LOOps ::
#Multiplication
# Multiplication tables from 1 to 10
'''for num in range(1, 11):    
    for i in range(1, 11):
        print(num * i, end=" ")
    print() 

num = 1
while num <= 10:
    i = 1
    while i <= 10:
        print(num * i, end=" ")
        i += 1
    print()
    num += 1'''
    
    
 # User a for loop to iterate over a list of number and prints each number squared     
'''numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(f"{num} squared is {num ** 2}")'''
    
    
    
# USes a while loop to find the sum of all odd number between 1 and 50    

num = 1
total = 0

while num <= 50:
    if num % 2 != 0:   
        total += num   
    num += 1           

print("Sum of odd numbers between 1 and 50 is:", total)


# USes a while loop to find the sum of all even  number between 1 and 50  
num = 0
total = 0

while num <= 50:
    if num % 2 == 0:   
        total += num   
    num += 1           

print("Sum of even numbers between 1 and 50 is:", total)



# Print all the number from1 to 50 except for multiple of 7 and use the continue statements to skip multiples of 7

for num in range(1, 51):   
    if num % 7 == 0:       
        continue        
    print(num)             

#Generate random number between 1 and 10 until a number greater than 7 is generated once such a number is generated program should print how many number were generated in total 


import random

count = 0  

while True:
    num = random.randint(1, 10)   
    count += 1                    
    print(f"Generated: {num}")   
    if num > 7:                   
        break

print(f"Total numbers generated: {count}")


