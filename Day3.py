#Create Unit Covertor 

'''print("---------------------------------------------------")
print("Welcome to the Unit Convertor")
print("1. Length")
print("2. Weight")
print("3. Temperature")
choice = int(input("Enter your choice (1-3): "))
if choice == 1:
    print("Length Convertor")
    print("1.Metre to Kilometre")
    print("2.Kilometer to Metre ")
    print("3.Metre to Centimetre")
    print("4. Centimetre to Metre")
    print("5.Kilometre to Centimetre")
    print("6.Centimetre to Kilometre")
    print("7. Feet to Metre")
    print("8.Metre to Feet")
    length_choice = int(input("Enter your choice (1-8): "))
    if length_choice == 1:
        metre = float(input("Enter length in metres: "))
        kilometre = metre / 1000
        print(f"{metre} metres is equal to {kilometre} kilometres.")
    elif length_choice == 2:
        kilometre = float(input("Enter length in kilometres: "))
        metre = kilometre * 1000
        print(f"{kilometre} kilometres is equal to {metre} metres.")
    elif length_choice == 3:
        metre = float(input("Enter length in metres: "))
        centimetre = metre * 100
        print(f"{metre} metres is equal to {centimetre} centimetres.")
    elif length_choice == 4:
        centimetre = float(input("Enter length in centimetres: "))
        metre = centimetre / 100
        print(f"{centimetre} centimetres is equal to {metre} metres.")
    elif length_choice == 5:
        kilometre = float(input("Enter length in kilometres: "))
        centimetre = kilometre * 100000
        print(f"{kilometre} kilometres is equal to {centimetre} centimetres.")
    elif length_choice == 6:
        centimetre = float(input("Enter length in centimetres: "))
        kilometre = centimetre / 100000
        print(f"{centimetre} centimetres is equal to {kilometre} kilometres.")
    elif length_choice == 7:
        feet = float(input("Enter length in feet: "))
        metre = feet * 0.3048
        print(f"{feet} feet is equal to {metre} metres.")
    elif length_choice == 8:
        metre = float(input("Enter length in metres: "))
        feet = metre / 0.3048
        print(f"{metre} metres is equal to {feet} feet.")
    else:
        print("Invalid choice for length conversion.")    
elif choice == 2:
    print("Weight Convertor")
    print("1.Kilogram to Gram")
    print("2.Gram to Kilogram")
    print("3.Kilogram to Pound")
    print("4.Pound to Kilogram")
    weight_choice = int(input("Enter your choice (1-4): "))
    if weight_choice == 1:
        kilogram = float(input("Enter weight in kilograms: "))
        gram = kilogram * 1000
        print(f"{kilogram} kilograms is equal to {gram} grams.")
    elif weight_choice == 2:
        gram = float(input("Enter weight in grams: "))
        kilogram = gram / 1000
        print(f"{gram} grams is equal to {kilogram} kilograms.")
    elif weight_choice == 3:
        kilogram = float(input("Enter weight in kilograms: "))
        pound = kilogram * 2.20462
        print(f"{kilogram} kilograms is equal to {pound} pounds.")
    elif weight_choice == 4:
        pound = float(input("Enter weight in pounds: "))
        kilogram = pound / 2.20462
        print(f"{pound} pounds is equal to {kilogram} kilograms.")
    else:
        print("Invalid choice for weight conversion.")
elif choice == 3:
    print("Temperature Convertor")
    print("1.Celsius to Fahrenheit")
    print("2.Fahrenheit to Celsius")
    print("3.Celsius to Kelvin")
    print("4.Kelvin to Celsius")
    temperature_choice = int(input("Enter your choice (1-4): "))
    if temperature_choice == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")
    elif temperature_choice == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius} degrees Celsius.")
    elif temperature_choice == 3:
        celsius = float(input("Enter temperature in Celsius: "))
        kelvin = celsius + 273.15
        print(f"{celsius} degrees Celsius is equal to {kelvin} Kelvin.")
    elif temperature_choice == 4:
        kelvin = float(input("Enter temperature in Kelvin: "))
        celsius = kelvin - 273.15
        print(f"{kelvin} Kelvin is equal to {celsius} degrees Celsius.")
    else:
        print("Invalid choice for temperature conversion.")
else:
    print("Invalid choice for unit conversion.")
print("---------------------------------------------------")'''
    
    


#Read an integer from the user and check if it is positive, negative or zero.
'''print("---------------------------------------------------")
print("Welcome to the Integer Checker")
number = int(input("Enter an integer: "))
if number > 0:
    print(f"{number} is a positive integer.")
elif number < 0:
    print(f"{number} is a negative integer.")
else:
    print("The number is zero.")
print("---------------------------------------------------")  '''




#Check if a year entered by the user is a leap year or not.and a leap year if it is divisible by 4 but not by 100, unless if it is also divisible by 400. pint appropriate message to the user.
'''print("---------------------------------------------------")
print("Welcome to the Leap Year Checker")
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
print("---------------------------------------------------")'''



#Ask the user for their pin if pin correct ask for withdraw amount if the amount exceed <=5000 print dispensing cash elsr print limit exceed  if pin is wrong print invalid pin 
'''print("---------------------------------------------------")
print("Welcome to the My ATM")
correct_pin = "1234"
pin = input("Enter your pin: ")
if pin == correct_pin:
    amount = float(input("Enter amount to withdraw: "))
    if amount <= 5000:
        print(f"Dispensing ${amount:.2f}")
        print("Please take your cash.")
        print("Thank you for using My ATM. Have a nice day!")
    else:
        print("Limit exceeded. Maximum withdrawal is $5000.")
else:
    print("Invalid pin. Sorry go out of my bank.")
print("---------------------------------------------------")'''


# Temperature Advisor: Ask the user for the current temperature in Celsius and provide advice on what to wear based on the temperature. For example, if the temperature is below 0°C, advise wearing a heavy coat; if it's between 0°C and 15°C, suggest wearing a jacket; if it's between 15°C and 25°C, recommend wearing a sweater; and if it's above 25°C, suggest wearing light clothing.
'''print("------------------------------------------------------------------------")
temperature = float(input("Enter the current temperature in Celsius: "))
if temperature < 0:
    print("It is very cold. You should wear a heavy coat.")
elif 0 <= temperature < 15:
    print("It is cool. You should wear a jacket.")
elif 15 <= temperature < 30:
    print("It is comfortable weather. You should wear a normal cloth.")
elif  temperature >30:
    print ("It is hot. You should wear light clothing and stay hydrated")

print("--------------------------------------------------------------------------")'''


#Create a loan Eligibility Checker ask for monthly income and existing emi if income >=30000and emi<0.4*income print for eligible for loan if income <30000 print income is too low if emi>=0.4*income print high debt burden print the reason in each case
'''print("---------------------------------------------------------------")
print("Welcome to the Loan Eligibility Checker")    
monthly_income = float(input("Enter your monthly income: "))
existing_emi = float(input("Enter your existing EMI: "))
if monthly_income >= 30000 and existing_emi < 0.4 * monthly_income:
    print("Congratulations! You are eligible for a loan.")
    print("Your income is sufficient and your existing EMI is within the acceptable limit.")
elif monthly_income < 30000:
    print("Sorry, your income is too low to be eligible for a loan.")
    print("Sorry your income is low  before applying for a loan.")

print("---------------------------------------------------------------")'''


#Build a number Guessing Hint Program the secret number is 42 ask the user to guess the number if the guess is correct print congratulations if the guess is too low print try a higher number if the guess is too high print try a lower number loop chlanai do jab tak number correct guess na kar lai or print how far off they are for wrong answer


'''print("---------------------------------------------------------------")
print("Welcome to the Number Guessing Game!")
secret_number = 42
while True:
    guess = int(input("Guess the secret number (between 1 and 100): "))
    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break
    elif guess < secret_number:
        print("Too low! Try a higher number.")
        a = secret_number - guess
        
    else:
        print("Too high! Try a lower number.")
        b = guess - secret_number
        print (b)
               
print("---------------------------------------------------------------")'''


# Classify a student performance : first check marks if marks>(pass/fail) if pass check >=90 "Distinction " >=75 "first devision" >=60"Second Division else third devision 
'''print("----------------------------------------------------------")
print("Welcome to Student Performance Dashboard ")
marks = float(input("Percentage of student: "))
if marks>=40 :
    print("Pass")
    if marks>= 90 :
        print("Distinction")
    elif marks>=75 :
        print("First Devision")
    elif marks>=60 :
        print("Second Devision")
    else:
        print("Third Devision ")            
else:
    print("Fail")    
    
print("--------------------------------------------------------------")    '''



#Create a Job Application Sceener 

'''print("----------------------------------------------------------------")
print("Welcome to Job Application Screener")
Age = int(input("Candidate age: "))
Degree = input("Degree of Candidate: ").strip()
CGPA = float(input("CGPA of Candidate: "))
if 21 <= Age <= 40:
    if Degree == "B.Tech" or Degree == "MCA":
        if CGPA >= 7.0:
            print("Interview Shortlisted")
        else:
            print("Application rejected: CGPA too low")
    else:
        print("Application rejected: Degree not eligible")
else:
    print("Application rejected: Age not in range 21-40")
    
print("---------------------------------------------------------------------")  '''


#E-Commerce Discount Calculator 
'''print("----------------------------------------------------------------")
print("Welcome to E-Commerce Discount Calculator ")  
Cart_Total = float(input("Cart Total : "))
Premium_member = input("Premium Member : ")
print(Cart_Total )

if Cart_Total>5000:
        if Premium_member == "Yes"  :
            print("Congratulation U got 5 percent extra Discount for premium membership ")
            
            Total_Discount = " Total Discount = 20 percent  "
            print(Total_Discount)
            Premium_memberdiscount =   20*Cart_Total/100
            print(Premium_memberdiscount)
            Final_cost = Cart_Total - Premium_memberdiscount
            print("Final cost =", Final_cost)
            
        else:
            Total_Discount= "15 percent discount"
            print (Total_Discount )
            discount= 15*Cart_Total /100
            Final_cost = Cart_Total - discount
            print("Final cost =", Final_cost)
            
            
else :
    Total_Discount= "10 percent discount"
    print(Total_Discount)
    discount =10*Cart_Total/100
    Final_cost = Cart_Total - discount
    print(discount)
    print("Final cost =", Final_cost)
    
print("----------------------------------------------------------------------------")   '''




    
    
                
            
            
         
            
             
    
    
    
  
  
  
  
    
    
    
    
    
           
        