'''a,b,c=2,5,5
print(b)

marks = float(input("Enter your marks: "))
print (marks)

x=99.255
print(type(x))

data=[5,"hi",3.5,False]
for item in data:
    print(type(item))'''



'''def detect_type(value_str):
    try:
        int(value_str)
        return int,int(value_str)
    except ValueError:
        pass
    try:
        float(value_str)
        return float,float(value_str)
    except ValueError:
        pass
    try:
        bool(value_str)
        return bool,bool(value_str)
    except ValueError:
        pass
    return str,value_str    

# Main program
user_input = input("Enter a value: ")
detected, converted_value = detect_type(user_input)
print(f"Type : {detected.__name__}")
print(f"Value: {converted_value}")
print(f"isinstance int? {isinstance(converted_value,int)}")'''


#Student information management system

'''Student_name = input("Enter student name: ")
Roll_number = input("Enter roll number: ")
Age = int (input("Enter age: "))
Program =input("Enter program: ")
CGPA = float(input("Enter CGPA: "))
Total_Courses = int(input("Enter total number of courses: "))
Completed_Courses = int(input("Enter number of completed courses: "))
Remaining_Courses = Total_Courses - Completed_Courses

print("Remaining courses: ",Remaining_Courses)
completion_percentage = (Completed_Courses / Total_Courses) * 100
print(f"Completion percentage: {completion_percentage:.2f}%")
if CGPA >=8.5:
    print("Eligible for scholarship")
else:
    print("Not eligible for scholarship")'''


# Smart Grade Analyzer

'''Maths_marks = float(input("Enter marks for Maths: "))
Physics_marks = float(input("Enter marks for Physics: "))
Chemistry_marks = float(input("Enter marks for Chemistry: "))
English_marks = float(input("Enter marks for English: "))
ComputerScience_marks = float(input("Enter marks for Computer Science: "))
total_marks = Maths_marks + Physics_marks + Chemistry_marks + English_marks + ComputerScience_marks
average_marks = total_marks / 5
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks:.2f}")
percentage = (total_marks / 500) * 100
print(f"Percentage: {percentage:.2f}%")
if percentage >= 90:
    print("Grade: A")
elif percentage >= 80:
    print("Grade: B")
elif percentage >= 70:
    print("Grade: C")
elif percentage >= 60:
    print("Grade: D")
else:
    print("Grade: F")'''
    

#Digital Shopping Cart
'''for i in range(1,6):
    print(f"\nEnter details for item {i}:")
    product_name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per unit: "))
    total_cost  = quantity * price
    print(f"Total cost for {quantity} {product_name}(s) is: ${total_cost:.2f}")
    Gst = total_cost * 0.18
    print(f"Gst(18%): ${Gst:.2f}")
    final_amount = total_cost + Gst
    print(f"Final amount to be paid: ${final_amount:.2f}")
    if final_amount > 50000:
        discount = final_amount * 0.10
        final_amount -= discount
    elif final_amount > 25000:
        discount = final_amount * 0.05
        final_amount -= discount
    print(f"Final amount after discount: ${final_amount:.2f}")'''
    
    
#Capst(one Assignment 

'''print("---------------------------------------------------------------")
print ("Welcome to the University Admission System!")
Student_name = input("Enter student name: ")
Age = int (input("Enter age: "))
Class12_percentage = float(input("Enter class 12 percentage: "))
Entrance_exam_score = float(input("Enter entrance exam score: "))
Category = input("Enter category (General/OBC/SC/ST): ")
if Category == "General":
    if Class12_percentage >= 90 and Entrance_exam_score >= 85:
        print("Eligible for admission &Scholarship")
    else:
        print("Not eligible for admission")
elif Category == "OBC":
    if Class12_percentage >= 85 and Entrance_exam_score >= 80:
        print("Eligible for admission &Scholarship")
    else:
        print("Not eligible for admission")
elif Category == "SC/ST":
    if Class12_percentage >= 80 and Entrance_exam_score >= 75:
        print("Eligible for admission &Scholarship")
    else:
        print("Not eligible for admission")
        
if Category == "General":
    if 90 <= Class12_percentage < 93:
        discount = 5
    elif 93 <= Class12_percentage < 95:
        discount = 10
    elif 95 <= Class12_percentage < 97:
        discount = 15
    elif 97 <= Class12_percentage <= 100:
        discount = 20
    else:
        discount = 0
elif Category == "OBC":
    if 85 <= Class12_percentage < 88:
        discount = 5
    elif 88 <= Class12_percentage < 90:
        discount = 10
    elif 90 <= Class12_percentage < 92:
        discount = 15
    elif 92 <= Class12_percentage <= 100:
        discount = 20
    else:
        discount = 0
elif Category == "SC/ST":
    if 80 <= Class12_percentage < 85:
        discount = 5
    elif 85 <= Class12_percentage < 90:
        discount = 10
    elif 90 <= Class12_percentage < 95:
        discount = 15
    elif 95 <= Class12_percentage <= 100:
        discount = 20
    else:
        discount = 0
else:
    discount = 0
print(f"Tuition fee discount: {discount}%")
print("---------------------------------------------------------------")'''



#Student Performance Dashboard

print("Student Performance Dashboard")
print("---------------------------------------------------------------")

Student_name = input("Enter student name: ")
Roll_number = input("Enter roll number: ")
Subjects = ["Maths", "Physics", "Chemistry", "English", "Computer Science"]
print("subjects: ",Subjects)
Maths_marks = float(input("Enter marks for Maths: "))
Physics_marks = float(input("Enter marks for Physics: "))
Chemistry_marks = float(input("Enter marks for Chemistry: "))
English_marks = float(input("Enter marks for English: "))
ComputerScience_marks = float(input("Enter marks for Computer Science: "))
totalsubject_marks = Maths_marks + Physics_marks + Chemistry_marks + English_marks + ComputerScience_marks
print(f"Total subject marks: {totalsubject_marks}")
Academic_percentage = (totalsubject_marks / 500) * 100
print(f"Academic percentage: {Academic_percentage:.2f}%")
Attandance_percentage = float(input("Enter attendance percentage: "))
if Attandance_percentage >= 75:
    print("Not Debbared")
else:
    print("Debbared")

    
#Subjects = ["Maths", "Physics", "Chemistry", "English", "Computer Science"]
#print("subjects: ",Subjects)
Mathsassignment_marks = float(input("Enter marks for MathsAssignment: "))
Physicsassignment_marks = float(input("Enter marks for PhysicsAssignment: "))
Chemistryassignment_marks = float(input("Enter marks for ChemistryAssignment: "))
Englishassignment_marks = float(input("Enter marks for EnglishAssignment: "))
ComputerScienceassignment_marks = float(input("Enter marks for Computer ScienceAssignment: "))
totalassignment_marks = Mathsassignment_marks + Physicsassignment_marks + Chemistryassignment_marks + Englishassignment_marks + ComputerScienceassignment_marks
print(f"Total assignment marks: {totalassignment_marks}")

Finalperformance_score = (totalsubject_marks ) + (totalassignment_marks )
print(f"Final Performance Score: {Finalperformance_score}")

Final_percentage = (Finalperformance_score / 1000) * 100
print(f"Final Percentage: {Final_percentage:.2f}%")

if Final_percentage >= 90:
    print("Grade: A")
elif Final_percentage >= 80:
    print("Grade: B")
elif Final_percentage >= 70:
    print("Grade: C")
elif Final_percentage >= 60:
    print("Grade: D")
else:
    print("Grade: F")
    
Results = "Pass" if Final_percentage >= 60 else "Fail"    
    
Category = input("Enter category (General/OBC/SC/ST): ")
if Category == "General":
    if Final_percentage >= 90 :
        print("Eligible for Scholarship")
    else:
        print("Not eligible for Scholarship")
elif Category == "OBC":
    if Final_percentage >= 85 :
        print("Eligible for Scholarship")
    else:
        print("Not eligible for Scholarship")
elif Category == "SC/ST":
    if Final_percentage >= 80 :
        print("Eligible for Scholarship")
    else:
        print("Not eligible for Scholarship")
        
if Category == "General":
    if 90 <= Final_percentage < 93:
        discount = 5
    elif 93 <= Final_percentage < 95:
        discount = 10
    elif 95 <= Final_percentage < 97:
        discount = 15
    elif 97 <= Final_percentage<= 100:
        discount = 20
    else:
        discount = 0
elif Category == "OBC":
    if 85 <= Final_percentage < 88:
        discount = 5
    elif 88 <= Final_percentage < 90:
        discount = 10
    elif 90 <= Final_percentage < 92:
        discount = 15
    elif 92 <= Final_percentage <= 100:
        discount = 20
    else:
        discount = 0
elif Category == "SC/ST":
    if 80 <= Final_percentage < 85:
        discount = 5
    elif 85 <= Final_percentage < 90:
        discount = 10
    elif 90 <= Final_percentage < 95:
        discount = 15
    elif 95 <= Final_percentage <= 100:
        discount = 20
    else:
        discount = 0
else:
    discount = 0
print(f"Tuition fee discount: {discount}%")
print("---------------------------------------------------------------")